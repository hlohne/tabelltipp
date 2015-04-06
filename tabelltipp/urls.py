from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from tabelltipp import settings

class MyRegistrationView(RegistrationView):
    form_class = RegistrationFormUniqueEmail

    def get_success_url(self, request, user):
        return '/'


urlpatterns = patterns('',
    url(r'^', include('tipp.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.ADMIN_ENABLED:
    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
        )

