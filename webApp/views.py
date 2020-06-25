from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from webApp.models import Treinamento
# Create your views here.

@login_required
def Treinamentos(request):
    return render(request, 'webApp/treinamento.html', {})
    

def index (request):
    treinamento = Treinamento.Objects.all()
    return render(request, 'treinamento.html', {'treinamento': treinamento})


def treino(request, treinamento_id):
    treinamento = Treinamento.Objects.get(pk=treinamento_id)
    return render(request, 'treinamentos.html', {'treinamento': treinamento})

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'