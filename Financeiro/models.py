from django.db import models
from webApp.models import Funcionario

class Financeiro(models.Model):
    funcionario = models.CharField(max_length=50)
    matricula_cemig = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    bco_ag_d_sal = models.IntegerField()
    cta_dep_sal = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    banco = models.CharField(max_length=25)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    operacao = models.IntegerField()
    numero_card = models.IntegerField()
    confirmado = models.DateField()

    class Meta:
        ordering = ('funcionario',)
        verbose_name_plural = 'financeiro'
    #------------RETORNO SELF PARA NOME E MATRICULA ------------
    def __str__(self):
        return self.matricula
   
