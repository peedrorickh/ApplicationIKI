from django.db import models
from django.conf import settings
from django.utils import timezone

class Cargo(models.Model):
    funcao = models.CharField(max_length=20)
    descricao = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.funcao


class Usuario(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
    matricula = models.CharField(max_length=7)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name

