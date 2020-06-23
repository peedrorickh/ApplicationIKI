from django.urls import path
from . import views
from django.conf.urls import url
from .views import IndexTemplateView
from django.views.generic import RedirectView


app_name = 'webApp'

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login/')),
    path('home/', IndexTemplateView.as_view(), name="index"),

    
    path('', views.usuario, name='users'),
    
]