from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView, CreateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

from webApp.forms import FuncionarioForm
from webApp.models import Funcionario, Treinamento


@login_required()
def cadastrar_funcionario(request):
    if not request.user.has_perm('webApp.add_funcionario'):
        return HttpResponse("Não há permissão para acessar essa página!")

    form = FuncionarioForm()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('webApp:index')

    return render(request, 'cadastrar_funcionario.html', {'form': form})


@login_required()
def adm_rh(request):
    return render(request, 'adm_rh.html')


@login_required()
def post_treinamento(request):
    treinamento = Treinamento.objects.all()
    return render(request, 'treinamento.html', {'post_treinamento': treinamento})


# ---------------- INDEX -----------------------#

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

# ----------------------------------------------#
