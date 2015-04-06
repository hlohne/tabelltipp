from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from urllib.request import urlopen
from datetime import datetime
from pytz import timezone


class Tabell(models.Model):
    navn = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    url = models.URLField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.navn)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.navn

    def reloaddata(self):
        error_occured = False
        timeinorge = datetime.now(timezone("Europe/Oslo")).hour
        try:
            assert(13 <= timeinorge < 22)
            f = urlopen(self.url).read().decode()
        except:
            return False

        for lag in Lag.objects.filter(tabell=self):
            try:
                stats = f.split("Hjemmetabell")[1].split(lag.navn.split()[0])[1].split("</tr>")[0].replace('\t','').replace('<td>','').replace('</td>','').splitlines()[1:9]
                lag.kamper_spilt = int(stats[0])
                lag.seire = int(stats[1])
                lag.uavgjort = int(stats[2])
                lag.tap = int(stats[3])
                lag.scoretemaal = int(stats[4])
                lag.maal = stats[4] + ' - ' + stats[5]
                lag.maalforskjell = int(stats[6])
                lag.poeng = int(stats[7].split('>')[1])
                lag.save()
            except:
                error_occured = True

        if error_occured:
            return False
        else:
            return True


class Lag(models.Model):
    navn = models.CharField(max_length=128, unique=True)
    poeng = models.IntegerField(default=0)
    kamper_spilt = models.IntegerField(default=0)
    seire = models.IntegerField(default=0, null=True)
    uavgjort = models.IntegerField(default=0, null=True)
    tap = models.IntegerField(default=0, null=True)
    maalforskjell = models.IntegerField(default=0)
    scoretemaal = models.IntegerField(default=0)
    maal = models.CharField(default='0 - 0', max_length=12, null=True)
    tabell = models.ForeignKey(Tabell)
    sorteringsnavn = models.CharField(max_length=128, null=True)

    def save(self, *args, **kwargs):
        self.sorteringsnavn = self.navn.lower().replace('aa', 'å')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.navn

    class Meta:
        ordering = ["-poeng", "-maalforskjell", "-scoretemaal", "kamper_spilt", "sorteringsnavn"]
        verbose_name_plural = 'lag'


class PoengRegel(models.Model):
    navn = models.CharField(max_length=128, unique=True)
    kortnavn = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.navn


class Liga(models.Model):
    navn = models.CharField(max_length=128, unique=True)
    public = models.BooleanField(default=True)
    tabell = models.ForeignKey(Tabell)
    poengregel = models.ForeignKey(PoengRegel)
    deltakere = models.ManyToManyField(User, through='Tabelltipp')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.navn)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.navn


class Tabelltipp(models.Model):
    user = models.ForeignKey(User, null=True)
    liga = models.ForeignKey(Liga, null=True)
    plassertlag = models.ManyToManyField(Lag, through='TippetPlassering')
    poeng = models.IntegerField(default=0)

    def getpoeng(self):
        poengid = self.liga.poengregel.kortnavn
        poengvektor = [tipp.getpoengfortipp() for tipp in TippetPlassering.objects.filter(tabelltipp=self)]

        if "kvadrat" in poengid:
            poengvektor = [poeng**2 for poeng in poengvektor]
            self.poeng = 1000-sum(poengvektor)

        else:
            self.poeng = 100-sum(poengvektor)

        self.save()

    class Meta:
        ordering = ["-poeng"]


class TippetPlassering(models.Model):
    lag = models.ForeignKey(Lag, null=True)
    tabelltipp = models.ForeignKey(Tabelltipp, null=True)
    tippet_plassering = models.IntegerField()

    def getpoengfortipp(self):
        poengid = self.tabelltipp.liga.poengregel.kortnavn
        lagitabell = Lag.objects.filter(tabell=self.lag.tabell)
        if "plassering" in poengid:
            plassitabell = [l.id for l in lagitabell].index(self.lag.id)+1
            return abs(plassitabell-int(self.tippet_plassering))

        elif "poeng" in poengid:
            return abs(self.lag.poeng-lagitabell[int(self.tippet_plassering)-1].poeng)

    class Meta:
        ordering = ["tippet_plassering"]
