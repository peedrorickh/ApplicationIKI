from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField


class Funcionario(models.Model):
    STATUS = (
                ('',''),
                ('ON', 'Ativo'),
                ('AW','Afastado'),
                ('VAC', 'Férias'),
                ('OFF','Desligado')
            )

    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, null= False, unique= True)
    rg = models.CharField(max_length=10)
    dt_nascimento = models.DateField()
    matricula_iki = models.CharField(max_length=5)
    matricula_cemig = models.CharField(max_length=7, null = False, unique=True)
    regiao = models.CharField(max_length=30)
    us = models.CharField(max_length=30)
    agencia = models.CharField(max_length=30)
    descricao = models.TextField(max_length=40)
    equipe = models.CharField(max_length=9)
    email = models.EmailField()
    dt_admissao = models.DateField()
    funcao = models.CharField(max_length=15)
    status = models.CharField(max_length=3, choices=STATUS, blank=False, null=False)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'funcionario'

    #------------RETORNO SELF PARA NOME E MATRICULA ------------#
    def __str__(self):
        return self.nome + ' ' +'(' +self.matricula_cemig + ')'


#------------MODELS CONTROLE ------------#
class Controle(models.Model):

    #---------CHOICES-----------#
    YES_NOT = (
        ('',''),
        ("S", "Sim"),
        ("S", "Não"),
    )
    
    #------------MODELS DB CONTROLE ------------#
    funcionario = models.CharField(max_length=50)
    matricula = models.CharField(max_length=7)
    pis = models.CharField(max_length=15)
    dias_semana = models.IntegerField()
    dias_pagar = models.IntegerField()
    vale_transporte = models.BooleanField()
    opcao = models.CharField(max_length=25)
    tarifa_ida = models.DecimalField(max_digits=3, decimal_places=2)
    tarifa_volta = models.DecimalField(max_digits=3, decimal_places=2)
    total_dia = models.IntegerField()
    saldo_mes = models.DecimalField(max_digits=3, decimal_places=2)
    recarregar = models.BooleanField()
    doc_pendente = models.BooleanField()
    folha_ponto = models.BooleanField()
    ferias_inicio = models.DateField()
    termino_ferias = models.DateField()
    ASO_periodico = models.CharField(max_length=1, choices=YES_NOT, blank=False, null=False)
    plano_saude = models.CharField(max_length=1, choices=YES_NOT, blank=False, null=False)
    plano_odonto = models.CharField(max_length=1, choices=YES_NOT, blank=False, null=False)

    #------------RETORNO SELF PARA NOME E MATRICULA ------------#
    def __str__(self):
        return '('+ self.matricula +')' + ' ' + self.funcionario


class DadosBancarios(models.Model):
    funcionario = models.CharField(max_length=50)
    matricula = models.CharField(max_length=7)
    bco_ag_d_sal = models.IntegerField()
    cta_dep_sal = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    banco = models.CharField(max_length=25)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    operacao = models.IntegerField()
    confirmado = models.DateTimeField(auto_now_add=False)
    numero_card = models.IntegerField()

    #------------RETORNO SELF PARA NOME E MATRICULA ------------
    def __str__(self):
        return '('+ self.matricula +')' + ' ' + self.funcionario


class Treinamento(models.Model):
    titulo = models.CharField(max_length=25, null=True, blank=False, unique=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resumo = RichTextField(max_length=20)
    dt_publicacao = models.DateField(auto_now=True)
    publicacao = RichTextField()

    #------------RETORNO SELF PARA NOME E MATRICULA ------------#
    def __str__(self):
        return self.titulo
    


class Prova(models.Model):
   
    titulo = models.ForeignKey(Treinamento,on_delete=models.SET_NULL,null=True)
    aluno = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    nota = models.IntegerField()
    
    
    #------------RETORNO SELF PARA NOME  ------------#
    def __str__(self):
        return str(self.aluno)
