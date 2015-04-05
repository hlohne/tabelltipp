from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from tipp.models import Lag, Liga, Tabell, Tabelltipp, TippetPlassering, PoengRegel
from tipp.forms import OpprettLiga
import simplejson as json
#import json

from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'tipp/index.html', {})

    user = request.user
    mine_ligaer = user.liga_set.all()
    for liga in mine_ligaer:
        liga.minplass = 1+Tabelltipp.objects.filter(liga=liga, poeng__gt=Tabelltipp.objects.get(user=user, liga=liga).poeng).count()

    return render(request, 'tipp/index.html', {'liga': mine_ligaer})


def tabell(request, tabell_slug):
    tabell = Tabell.objects.get(slug=tabell_slug)
    lag = Lag.objects.filter(tabell=tabell)
    tabell.lag = lag
    context_dict = {'tabell': tabell}
    return render(request, 'tipp/tabell.html', context_dict)


def ligaer(request):
    liga_list = Liga.objects.filter(public=True)
    for l in liga_list:
        l.antall = User.objects.filter(tabelltipp__liga=l).count()
    context_dict = {'ligaer': liga_list}

    return render(request, 'tipp/ligaer.html', context_dict)

@login_required
def liga(request, liganavn_slug):
    context_dict = {}
    try:
        liga = Liga.objects.get(slug=liganavn_slug)
        context_dict['liganavn'] = liga.navn

        tabelltipp = Tabelltipp.objects.filter(liga=liga)
        for tipp in tabelltipp:
            tipp.getpoeng()

        tabelltipp = Tabelltipp.objects.filter(liga=liga)
        for d in tabelltipp:
            d.sinplass = 1+Tabelltipp.objects.filter(liga=liga, poeng__gt=Tabelltipp.objects.get(user=d.user, liga=liga).poeng).count()
        context_dict['tabelltipp'] = tabelltipp
        context_dict['liga'] = liga

        deltakere = liga.deltakere.all()
        if request.user in deltakere:
            context_dict['userinliga'] = True

    except Liga.DoesNotExist:
        pass

    return render(request, 'tipp/liga.html', context_dict)


@login_required
def opprett_liga(request):
    if request.method == "POST":
        form = OpprettLiga(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            try:
                ligaobject=form.save(commit=True)
                return blimediliga(request, ligaobject.slug)

            except:
                pass
    else:
        form = OpprettLiga()

    tabeller = Tabell.objects.all()
    poengregler = PoengRegel.objects.all()
    context_dict = {"form": form, "tabeller": tabeller, "poengregler": poengregler}

    return render(request, 'tipp/opprettliga.html', context_dict)


@login_required
def blimediliga(request, liga_slug):
    liga = Liga.objects.get(slug=liga_slug)
    lag = Lag.objects.filter(tabell=liga.tabell)
    context_dict = {'lag': lag, 'liga': liga}
    return render(request, 'tipp/blimediliga.html', context_dict)


@login_required
def blimediligaform(request):
    if request.method == 'GET':
        ligaid = request.GET['ligaid']
        ordning = [int(i) for i in str(request.GET['ordning']).split('_')]
        user = request.user
        tabelltipp = Tabelltipp()
        tabelltipp.user = user
        tabelltipp.liga = Liga.objects.get(id=ligaid)
        tabelltipp.save()
        for tippetplassering, lagid in enumerate(ordning):
            tipp = TippetPlassering()
            tipp.lag = Lag.objects.get(id=lagid)
            tipp.tabelltipp = tabelltipp
            tipp.tippet_plassering = tippetplassering+1
            tipp.save()
    return ligaer(request)


@login_required
def se_tipp(request, liga_slug, user_slug):
    user = request.user
    brukeren = User.objects.get(username=user_slug).username
    ligaen = Liga.objects.get(slug=liga_slug)
    if user not in ligaen.deltakere.all():
        messages.add_message(request, messages.INFO, brukeren)
        return redirect('liga',ligaen.slug)
    tabelltipp = Tabelltipp.objects.filter(user__username=user_slug, liga__slug=liga_slug).first()
    plassertlag=TippetPlassering.objects.filter(tabelltipp=tabelltipp).all()
    return render(request, 'tipp/se_tipp.html', {'tabelltipp': tabelltipp, 'plassertlag': plassertlag})

def test(request):
    return render(request, 'tipp/test.html', {})

@login_required
def testmetode(request):
    lagid = request.GET["lagid"]
    tabelltippid = request.GET["tabelltippid"]

    lag = Lag.objects.get(id=lagid)
    lagitabell = Lag.objects.filter(tabell=lag.tabell).all()
    plassitabell = [l.id for l in lagitabell].index(lag.id)+1
    poeng = lag.poeng
    tabelltipp = Tabelltipp.objects.get(id=tabelltippid)
    print(tabelltipp)
    tipp = TippetPlassering.objects.get(tabelltipp=tabelltipp, lag=lag)
    print(tipp)
    minuspoeng = tipp.getpoengfortipp()
    print(minuspoeng)

    results = {"plass": str(plassitabell), "poeng": str(poeng), "minuspoeng": str(minuspoeng)}
    return HttpResponse(json.dumps(results))
