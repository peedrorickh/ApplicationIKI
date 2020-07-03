from django.shortcuts import render
from Financeiro.models import Financeiro
# Create your views here.

def financeiro(request):
    financeiro = Financeiro.objects.all()
    return render(request, 'webApp/adm_rh.html', {'financeiro': financeiro})

