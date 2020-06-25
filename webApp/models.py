from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField

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