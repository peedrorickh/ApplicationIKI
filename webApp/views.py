from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from webApp.forms import FuncionarioForm
from webApp.models import Treinamento
from webApp.models import Noticia


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


# ----- listar treinamento -----#
@login_required()
def post_treinamento(request):
    treinamento = Treinamento.objects.all()
    return render(request, 'treinamento.html', {'treinamento': treinamento})


# ----- leitura de treinamento mais detalhado -----#
@login_required()
def details_treinamento(request, pk):
    treinamento = get_object_or_404(Treinamento, pk=pk)
    return render(request, 'details_treinamento.html', {'treinamento': treinamento})


# ---------------- INDEX-HOMEPAGE -----------------------#

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def teste(noticia):
        noticia = Noticia.objects.last()
        return noticia

# ----------------------------------------------#

@login_required()
def noticia(request):
    noticia = Noticia.objects.all()
    return render(request,'noticia.html', {'noticia':noticia})
