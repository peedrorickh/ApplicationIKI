from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import io

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

def cadastrar_funcionario(request):

    form = FuncionarioForm()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if(form.is_valid()):
            post_nome = form.cleaned_data['nome']
            post_cpf = form.cleaned_data['cpf']
            post_rg = form.cleaned_data['rg']
            post_dt_nascimento = form.cleaned_data['dt_nascimento']
            post_matricula_iki = form.cleaned_data['matricula_iki']
            func_name = form.cleaned_data['matricula_cemig']
            func_name = form.cleaned_data['regiao']
            func_name = form.cleaned_data['us']
            func_name = form.cleaned_data['agencia']
            func_name = form.cleaned_data['descricao']
            func_name = form.cleaned_data['equipe']
            func_name = form.cleaned_data['email']
            func_name = form.cleaned_data['dt_admissao']
            func_name = form.cleaned_data['funcao']
            func_name = form.cleaned_data['status']

        form.save()
        return redirect('webApp:index')
    return render(request, 'cadastrar_funcionario.html', {'form': form})

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    