from django.urls import path
from . import views
from django.conf.urls import url, include


from .views import IndexTemplateView, cadastrar_funcionario, post_treinamento, details_treinamento, noticia
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from Financeiro.views import adm_rh

app_name = 'webApp'

urlpatterns = [
                  path('logon/', RedirectView.as_view(url='/accounts/login/')),
                  path('', IndexTemplateView.as_view(), name="index"),
                  path('ckeditor', include('ckeditor_uploader.urls')),
                  path('noticia/', noticia , name='noticia'),
                  path('criar/funcionario/', cadastrar_funcionario, name='cadastrar_funcionario'),
                  path('adm/rh/', adm_rh, name='adm_rh'),
                  path('post/treinamento', post_treinamento, name='post_treinamento'),
                  path('post/<int:pk>/', views.details_treinamento, name='details_treinamento')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
