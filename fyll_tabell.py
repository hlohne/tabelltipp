import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tabelltipp.settings')

import django
django.setup()

from tipp.models import Lag, Tabell


def populate():
    tippeligaen = Tabell(navn='Tippeligaen')
    tippeligaen.save()
    legg_til_lag("Bodø/Glimt", tippeligaen)
    legg_til_lag("Haugesund", tippeligaen)
    legg_til_lag("Mjøndalen", tippeligaen)
    legg_til_lag("Molde", tippeligaen)
    legg_til_lag("Odd", tippeligaen)
    legg_til_lag("Rosenborg", tippeligaen)
    legg_til_lag("Sandefjord", tippeligaen)
    legg_til_lag("Sarpsborg 08", tippeligaen)
    legg_til_lag("Stabæk", tippeligaen)
    legg_til_lag("Start", tippeligaen)
    legg_til_lag("Strømsgodset", tippeligaen)
    legg_til_lag("Tromsø", tippeligaen)
    legg_til_lag("Viking", tippeligaen)
    legg_til_lag("Vålerenga", tippeligaen)
    legg_til_lag("Aalesund", tippeligaen)
    legg_til_lag("Lillestrøm", tippeligaen,-1, 0)

    obosligaen = Tabell(navn='OBOS-ligaen')
    obosligaen.save()
    legg_til_lag("Brann", obosligaen, 0)
    legg_til_lag("Bryne", obosligaen,0)
    legg_til_lag("Bærum", obosligaen,0)
    legg_til_lag("Follo", obosligaen,0)
    legg_til_lag("Fredrikstad", obosligaen, 0)
    legg_til_lag("Hødd", obosligaen, 0)
    legg_til_lag("Hønefoss", obosligaen,0)
    legg_til_lag("Jerv", obosligaen,0)
    legg_til_lag("Kristiansund BK", obosligaen,0)
    legg_til_lag("Levanger", obosligaen,0)
    legg_til_lag("Nest-Sotra", obosligaen,0)
    legg_til_lag("Ranheim", obosligaen,0)
    legg_til_lag("Strømmen", obosligaen,0)
    legg_til_lag("Sandnes Ulf", obosligaen,0)
    legg_til_lag("Sogndal", obosligaen,0)
    legg_til_lag("Åsane", obosligaen,0, 0)


    # Print out what we have added to the user.
    for l in Lag.objects.all():
        print("{0}".format(str(l)))
'''
def populate():

    # Print out what we have added to the user.
    for l in Lag.objects.all():
        print("{0}".format(str(l)))
'''
def legg_til_lag(navnet, ligaen, antallpoeng=0, kamperspilt=0):
    l = Lag.objects.get_or_create(navn=navnet, tabell=ligaen)[0]
    l.poeng=antallpoeng
    l.kamper_spilt=kamperspilt
    l.save()
    return l

# Start execution here!
if __name__ == '__main__':
    print("Legger inn lag...")
    populate()
