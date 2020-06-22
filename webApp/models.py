from django.db import models
from django.conf import settings
from django.utils import timezone


class Usuario(models.Model):
    matricula = models.CharField(max_length=7)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
