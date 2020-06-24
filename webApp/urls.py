from django.urls import path
from . import views
from django.conf.urls import url, include
from .views import IndexTemplateView
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'webApp'

urlpatterns = [
    path('home/', RedirectView.as_view(url='/accounts/login/')),
    path('', IndexTemplateView.as_view(), name="index"),
    path('treinamentos/', views.Treinamentos, name='treinamentos'),
    path('ckeditor', include('ckeditor_uploader.urls'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)