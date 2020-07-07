from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField


class Agencia(models.Model):
    agencia = models.CharField(max_length=25)

    def __str__(self):
        return self.agencia


class Regiao(models.Model):
    regiao = models.CharField(max_length=25)

    def __str__(self):
        return self.regiao


class Us(models.Model):
    us = models.CharField(max_length=25)

    def __str__(self):
        return self.us


class Funcionario(models.Model):
    STATUS = (
        ('', ''),
        ('ON', 'Ativo'),
        ('AW', 'Afastado'),
        ('VAC', 'Férias'),
        ('OFF', 'Desligado')
    )

    matricula_iki = models.CharField(max_length=5, primary_key=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    rg = models.CharField(max_length=10)
    dt_nascimento = models.DateField()
    nome_pai = models.CharField(max_length=30)
    nome_mae = models.CharField(max_length=30)
    pis = models.IntegerField()
    regiao = models.ForeignKey(Regiao, on_delete=models.SET_NULL, null=True)
    us = models.ForeignKey(Us, on_delete=models.SET_NULL, null=True)
    agencia = models.ForeignKey(Agencia, on_delete=models.SET_NULL, null=True)
    equipe = models.CharField(max_length=9)
    email = models.EmailField()
    status = models.CharField(max_length=3, choices=STATUS, blank=False, null=False)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'funcionario'

    # ------------RETORNO SELF PARA NOME E MATRICULA ------------#
    def __str__(self):
        return self.matricula_iki


# ------------MODELS CONTROLE ------------#
class Controle(models.Model):
    # ---------CHOICES-----------#
    YES_NOT = (
        ('', ''),
        ("S", "Sim"),
        ("S", "Não"),
    )
    FOLHA_PONTO = (
        ('ENT','ENTREGUE'),
        ('DIA','EM DIA'),
        ('ATR','COM ATRASO'), 
        ('PEN','PENDENTE')
    )
    PEN_ENT =(
        ('PEN','PENDENTE'),
        ('ENT','ENTREGUE')
    )

    # ------------MODELS DB CONTROLE ------------#
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
    Doc_contratação = models.CharField(max_length=3, choices=PEN_ENT, blank=False, null=False)
    Doc_admissão = models.CharField(max_length=3 ,choices=PEN_ENT, blank=False, null=False)
    Doc_demissão = models.CharField(max_length=3 ,choices=PEN_ENT, blank=False, null=False)
    folha_ponto = models.CharField(max_length=3 ,choices=FOLHA_PONTO, blank=False, null=False)
    ferias_inicio = models.DateField()
    termino_ferias = models.DateField()
    ASO_periodico = models.CharField(max_length=1, choices=YES_NOT, blank=False, null=False)
    plano_saude = models.CharField(max_length=1, choices=YES_NOT, blank=False, null=False)
    plano_odonto = models.CharField(max_length=1, choices=YES_NOT, blank=False, null=False)

    # ------------RETORNO SELF PARA NOME E MATRICULA ------------#
    def __str__(self):
        return '(' + self.matricula + ')' + ' ' + self.funcionario


class Treinamento(models.Model):
    titulo = models.CharField(max_length=25,    
                              null=True, 
                              blank=False, 
                              unique=True
                              )
    autor = models.ForeignKey(User, 
                              on_delete=models.SET_NULL, 
                              null=True
                              )
    resumo = RichTextField(max_length=20)
    dt_publicacao = models.DateField(auto_now=True)
    publicacao = RichTextField()

    # ------------RETORNO SELF PARA NOME E MATRICULA ------------#
    def __str__(self):
        return self.titulo


class Prova(models.Model):
    titulo = models.ForeignKey(Treinamento, 
                               on_delete=models.SET_NULL, 
                               null=True
                               )
    aluno = models.ForeignKey(Funcionario, 
                              on_delete=models.SET_NULL,
                               null=True
                               )
    nota = models.IntegerField()

    # ------------RETORNO SELF PARA NOME  ------------#
    def __str__(self):
        return str(self.aluno)

class Noticia(models.Model):
    titulo = models.CharField(max_length=55)
    dt_publicação = models.DateField(auto_now=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, 
                            null=True
                            )
    noticia = RichTextField()

    def __str__(self):
        return self.titulo
    