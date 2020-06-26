from django.urls import path
#from . import views
from django.conf.urls import url, include
from .views import IndexTemplateView, cadastrar_funcionario
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'webApp'

urlpatterns = [
    path('logon/', RedirectView.as_view(url='/accounts/login/')),
    path('', IndexTemplateView.as_view(), name="index"),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('criar/funcionario/', cadastrar_funcionario, name='cadastrar_funcionario')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)