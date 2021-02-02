from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 30)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        "contatos": contatos,
    })


def detalhes(request, contato_id):
    contato = Contato.objects.get(id=contato_id)

    return render(request, 'contatos/detalhes.html', {
        "contato": contato,
    })