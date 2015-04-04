from django.conf.urls import patterns, include, url
from django.shortcuts import redirect
from django.contrib import admin
from django.contrib import messages
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

class MyRegistrationView(RegistrationView):
    form_class = RegistrationFormUniqueEmail

    def get_success_url(self, request, user):
        return '/tipp/'

    def register(self, request, **cleaned_data):
        print("hei")
        user = super().register(request, **cleaned_data)
        print(user)

        if user:
            print("Nå kom vi her")
            return user

        else:
            messages.add_message(request, messages.INFO, "Dette er en melding")
            print("Sender melding")
            return redirect('register_registration')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tabelltipp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tipp/', include('tipp.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
