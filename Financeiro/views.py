from django.shortcuts import render
from Financeiro.models import Financeiro
# Create your views here.

def adm_rh(request):
    financeiro = Financeiro.objects.all()
    return render(request, 'adm_rh.html', {'financeiro': financeiro})

