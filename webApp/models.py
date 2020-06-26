from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField

#Primeiro teste Models
"""
#Model para atribuir Cargos
class Cargo(models.Model):
    funcao = models.CharField(max_length=20)
    descricao = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.funcao

#Model para atribuir usuarios
class Usuario(models.Model):
    cargo = models.ForeignKey(GROU)
    matricula = models.CharField(max_length=7)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    

    def __str__(self):
        return self.first_name

#Model Para publicar Treinamento

class Treinamento(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Teste postagem treinamento like a blog

class Post(models.Model):
    titile = models.CharField(max_length=255)
    resume = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.titile

"""

#Segundo teste Models
"""
class Cargo(models.Model):
    funcao = models.CharField(max_length=20)
    descricao = models.TextField(max_length=50)

    def __str__(self):
         return self.funcao

class US(models.Model):
    regiao = models.CharField(max_length=15)
    us = models.CharField(max_length=15)
    agencia = models.CharField(max_length=15)

    def __str__(self):
        return self.us

class Funcionario(models.Model):
    cpf = models.IntegerField(verbose_name='cpf' , null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=9)
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    matricula = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
    us = models.ForeignKey(US, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.primeiro_nome

class Treinamento(models.Model):
    titulo =  models.CharField(max_length=25, null=False, blank=False, unique=True)
    autor = models.CharField(max_length=20)
    resumo = RichTextField()
    dt_publicacao = models.DateField(auto_now=True)
    publicacao = RichTextField()
    
    def __str__(self):
        return self.titulo

class Prova(models.Model):
        nota = models.IntegerField()
        titulo = models.ForeignKey(Treinamento, on_delete=models.SET_NULL, null=True)
        aluno = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
        
        def __str__(self):
            return (str(self.aluno))
"""

#Terceito teste models

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    dt_nascimento = models.DateField()
    matricula_iki = models.CharField(max_length=5)
    matricula_cemig = models.CharField(max_length=7)
    regiao = models.CharField(max_length=30)
    us = models.CharField(max_length=30)
    agencia = models.CharField(max_length=30)
    descricao = models.TextField(max_length=40)
    equipe = models.CharField(max_length=9)
    email = models.EmailField()
    dt_admissao = models.DateField()
    funcao = models.CharField(max_length=15)
    status = models.BooleanField()

    def __str__(self):
        return self.nome

class Controle(models.Model):
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
    ASO_periodico = models.BooleanField()
    plano_saude = models.BooleanField()
    plano_odonto = models.BooleanField()

    def __str__(self):
        return self.matricula

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
    confirmado = models.BooleanField()
    numero_card = models.IntegerField()

    def __str__(self):
        return self.matricula

class Treinamento(models.Model):
    titulo = models.CharField(max_length=25, null=False, blank=False, unique=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resumo = RichTextField()
    dt_publicacao = models.DateField(auto_now=True)
    publicacao = RichTextField()

    def __str__(self):
        return self.titulo


class Prova(models.Model):
    nota = models.IntegerField()
    titulo = models.ForeignKey(Treinamento, on_delete=models.SET_NULL, null=True)
    aluno = models.ForeignKey(Funcionario,  on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return (str(self.aluno))
        

