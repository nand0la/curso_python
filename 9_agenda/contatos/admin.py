from django.contrib import admin
from .models import Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    """
        classe usada para adicionar configurações de display
    """
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'mostrar', 'categoria')
    list_editable = ('telefone', 'mostrar')
    list_display_links = ('nome', 'sobrenome')



admin.site.register(Contato, ContatoAdmin)
