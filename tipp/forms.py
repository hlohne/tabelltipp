from django.forms import ModelForm
from tipp.models import Liga

class OpprettLiga(ModelForm):
    class Meta:
        model = Liga
        fields = ('navn', 'tabell', 'poengregel')

from django import forms

class ExampleForm(forms.Form):
    username = forms.CharField(max_length=30, label=u'Username')
    email = forms.EmailField(label=u'Email address')