from django.shortcuts import render, get_object_or_404
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()

    return render(request, 'home/index.j2', {
        "contatos": contatos
    })
    

def ver_contato(request, id_contato):
    contato = get_object_or_404(Contato, id_contato=id_contato)

    return render(request, 'home/contato.j2', {
        "contato": contato
    })
    