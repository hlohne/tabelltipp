from django.conf.urls import patterns, include, url
from django.shortcuts import redirect
from django.contrib import admin
from django.contrib import messages
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

class MyRegistrationView(RegistrationView):
    form_class = RegistrationFormUniqueEmail

    def get_success_url(self, request, user):
        return '/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tabelltipp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tipp.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
