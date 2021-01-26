from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "sobrenome", "telefone", "categoria", "mostrar")
    list_editable = ("telefone", "mostrar")

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "categoria")

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria, CategoriaAdmin)