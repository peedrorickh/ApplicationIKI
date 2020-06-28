from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView, CreateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

from webApp.forms import FuncionarioForm
from webApp.models import Funcionario

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


@login_required()
def cadastrar_funcionario(request):
    form = FuncionarioForm()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('webApp:index')

    return render(request, 'cadastrar_funcionario.html', {'form': form})


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
