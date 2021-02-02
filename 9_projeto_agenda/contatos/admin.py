from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "telefone", "mostrar")
    list_editable = ("mostrar", "telefone")

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "categoria")


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
