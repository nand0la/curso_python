from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BLANK_CHOICE_DASH


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    mostrar = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
