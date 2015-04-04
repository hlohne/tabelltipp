from django.conf.urls import patterns, url
from tipp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^tabell/(?P<tabell_slug>[\w\-]+)/$', views.tabell, name='tabell'),
                       url(r'^ligaer/$', views.ligaer, name='ligaer'),
                       url(r'^blimediliga/(?P<liga_slug>[\w\-]+)/$', views.blimediliga, name='blimediliga'),
                       url(r'^blimediligaform/$', views.blimediligaform, name='blimediligaform'),
                       url(r'^opprettliga/$', views.opprett_liga, name='opprettliga'),
                       url(r'^liga/(?P<liganavn_slug>[\w\-]+)/$', views.liga, name='liga'),
                       url(r'^se_tipp/(?P<liga_slug>[\w\-]+)/(?P<user_slug>[\w\-]+)/$', views.se_tipp, name='se_tipp'),
                       url(r'^test/$', views.test, name='test'),
                       )
