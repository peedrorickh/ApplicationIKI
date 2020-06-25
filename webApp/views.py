from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import io
from webApp.models import Treinamento
# Create your views here.

"""
@login_required
def Treinamento(request):
    treinamento = Treinamento.objects.all()
    return render(request, 'webApp/treinamento.html', {'treinamento' : treinamento})
    

def index (request):
    treinamento = Treinamento.objects.all()
    return render(request, 'treinamento.html', {'treinamento': treinamento})


def treino(request, treinamento_id):
    treinamento = Treinamento.objects.get(pk=treinamento_id)
    return render(request, 'treinamento.html', {'treinamento': treinamento})
"""

def resumo(request):
        treinamento = Treinamento.objects.all()
        return render(request, 'index.html', {'Treinamento' : treinamento})

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    