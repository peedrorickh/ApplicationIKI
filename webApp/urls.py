from django.urls import path
from . import views
from django.conf.urls import url, include
from .views import IndexTemplateView
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'webApp'

urlpatterns = [
    path('logon/', RedirectView.as_view(url='/accounts/login/')),
    path('', IndexTemplateView.as_view(), name="index"),
   # path('treinamento/', views.Treinamento, name='treinamento'),
    path('ckeditor', include('ckeditor_uploader.urls')),
   # path('treinamentos/<int>=:treinamento_id>', views.treino),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)