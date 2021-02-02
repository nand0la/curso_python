from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.categoria    


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    mostrar = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome