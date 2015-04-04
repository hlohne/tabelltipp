from django import template
from django.core.urlresolvers import reverse
from tipp.models import Tabell

register = template.Library()

@register.simple_tag
def navactive(request, urls, **kwargs):
  try:
    if request.path in ( reverse(url, **kwargs) for url in urls.split() ):
      return 'active'
    return ''
  except:
    return ''

@register.inclusion_tag("tipp/dropdownmenu.html")
def gettabeller(a):
  tabeller = Tabell.objects.all()
  return {'tabeller': tabeller}


@register.inclusion_tag("tipp/signup.html")
def signup(request):
  if request.path in (reverse('registration_register'), reverse('auth_logout'),reverse('auth_login')):
    return {}
  else:
    return {'signup': True}
