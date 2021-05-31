from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone

"""
    models são classes no nosso código que refernciam tabelas no BD
    usadas em ORM (Django ORM)
"""


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True) 
    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome
        

class Contato(models.Model):
    id_contato = models.IntegerField(primary_key=True) 
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.nome