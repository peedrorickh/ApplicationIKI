from django.urls import path
from . import views
from django.conf.urls import url
from .views import IndexTemplateView
from django.views.generic import RedirectView


app_name = 'webApp'

urlpatterns = [
    path('home/', RedirectView.as_view(url='/accounts/login/')),
    path('', IndexTemplateView.as_view(), name="index"),
    path('treinamentos/', views.Treinamentos, name='treinamentos'),
    
]