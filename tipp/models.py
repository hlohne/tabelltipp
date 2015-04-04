from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class Tabell(models.Model):
    navn = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.navn)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.navn


class Lag(models.Model):
    navn = models.CharField(max_length=128, unique=True)
    poeng = models.IntegerField(default=0)
    kamper_spilt = models.IntegerField(default=0)
    maalforskjell = models.IntegerField(default=0)
    scoretemaal = models.IntegerField(default=0)
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
        if "plassering" in poengid:
            poengvektor = []
            for plass,lag in enumerate(self.plassertlag.all()):
                tippetplass = TippetPlassering.objects.get(lag=lag, tabelltipp=self).tippet_plassering
                poengvektor.append(abs(plass+1-tippetplass))

            if "kvadrat" in poengid:
                poengvektor = [poeng**2 for poeng in poengvektor]
            self.poeng = 1000-sum(poengvektor)/2
            self.save()

        elif "poeng" in poengid:
            tabelloversikt = self.plassertlag.all()
            poengvektor = [abs(lag.poeng-tabelloversikt[TippetPlassering.objects.get(lag=lag, tabelltipp=self).tippet_plassering-1].poeng) for lag in tabelloversikt]

            if "kvadrat" in poengid:
                poengvektor = [poeng**2 for poeng in poengvektor]
            self.poeng = 1000-sum(poengvektor)/2
            self.save()

    class Meta:
        ordering = ["-poeng"]


class TippetPlassering(models.Model):
    lag = models.ForeignKey(Lag, null=True)
    tabelltipp = models.ForeignKey(Tabelltipp, null=True)
    tippet_plassering = models.IntegerField()

    class Meta:
        ordering = ["tippet_plassering"]
