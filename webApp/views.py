from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def Treinamentos(request):
    return render(request, 'webApp/treinamento.html', {})


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'