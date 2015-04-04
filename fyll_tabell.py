import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tabelltipp.settings')

import django
django.setup()

from tipp.models import Lag, Tabell


def populate():
    obosligaen = Tabell(navn='OBOS-ligaen')
    obosligaen.save()
    legg_til_lag("Brann", obosligaen, 50)
    legg_til_lag("Bryne", obosligaen,2)
    legg_til_lag("Bærum", obosligaen,4)
    legg_til_lag("Follo", obosligaen,36)
    legg_til_lag("Fredrikstad", obosligaen, 35)
    legg_til_lag("Hødd", obosligaen, 4)
    legg_til_lag("Hønefoss", obosligaen,8)
    legg_til_lag("Jerv", obosligaen,11)
    legg_til_lag("Kristiansund BK", obosligaen,44)
    legg_til_lag("Levanger", obosligaen,33)
    legg_til_lag("Nest-Sotra", obosligaen,22)
    legg_til_lag("Ranheim", obosligaen,15)
    legg_til_lag("Strømmen", obosligaen,17)
    legg_til_lag("Sandnes Ulf", obosligaen,27)
    legg_til_lag("Sogndal", obosligaen,9)
    legg_til_lag("Åsane", obosligaen,0, 0)

    # Print out what we have added to the user.
    for l in Lag.objects.all():
        print("{0}".format(str(l)))
'''
def populate():
    obosligaen = Tabell(navn='Tippeligaen')
    obosligaen.save()
    legg_til_lag("Bodø/Glimt", obosligaen)
    legg_til_lag("Haugesund", obosligaen)
    legg_til_lag("Mjøndalen", obosligaen)
    legg_til_lag("Molde", obosligaen)
    legg_til_lag("Odd", obosligaen)
    legg_til_lag("Rosenborg", obosligaen)
    legg_til_lag("Sandefjord", obosligaen)
    legg_til_lag("Sarpsborg 08", obosligaen)
    legg_til_lag("Stabæk", obosligaen)
    legg_til_lag("Start", obosligaen)
    legg_til_lag("Strømsgodset", obosligaen)
    legg_til_lag("Tromsø", obosligaen)
    legg_til_lag("Viking", obosligaen)
    legg_til_lag("Vålerenga", obosligaen)
    legg_til_lag("Aalesund", obosligaen)
    legg_til_lag("Lillestrøm", obosligaen,-1, 0)

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


def leggbrukere_i_liga():
  from django.contrib.auth.models import User
  from tipp.models import Liga, Medlemskap
  User
  User.objects.all()
  User.objects.filter(username="henning")
  henning=User.objects.filter(username="henning")
  mads=User.objects.filter(username="mads")
  paal=User.objects.filter(username="pål")
  eirik=User.objects.filter(username="eirik")
  Liga.objects.all()
  minliga=Liga.objects.all()[0]
  dinliga=Liga.objects.all()[1]
  x1=Medlemskap()
  x1.user=henning
  henning
  henning[0]
  henning=henning[0]
  mads=mads[0]
  paal=paal[0]
  eirik=eirik[0]
  x1
  x1.user=henning
  minliga
  x1.liga=minliga
  x1.save()
  x2=Medlemskap()
  x2.user=mads
  x2.liga=minliga
  x2.save()
  x3=Medlemskap()
  x3.user=paal
  x3.liga=minliga
  x3.save()
  x4=Medlemskap()
  x4.user=eirik
  x4.liga=minliga
  x4.save()
  x5=Medlemskap()
  x5.user=henning
  x5.liga=dinliga
  x5.save()
  x6=Medlemskap()
  x6.user=eirik
  x6.liga=dinliga
  x6.save()



# Start execution here!
if __name__ == '__main__':
    print("Legger inn lag...")
    populate()
