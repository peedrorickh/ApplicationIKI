from django import template
from webApp.models import Noticia

register = template.Library()

@register.simple_tag
def noticias():
    
    noticias = Noticia.objects.all()
    return noticias