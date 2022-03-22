from django.db import models

# Create your models here.


class Agente(models.Model):
    Nome = models.CharField(max_length=150)
    Classe = models.CharField(max_length=100)
    Função = models.CharField(max_length=100)
