from django.core import paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Contato
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contatos = Contato.objects.all()  # orm django - retorna lista com todos os dados
    paginator = Paginator(contatos, 10)  # limitando os contatos

    page = request.GET.get('page')  # vai pegar o parametro get page enviado pela url com o numero da pagina
    contatos = paginator.get_page(page)  # retona o objeto contato mais indice de paginas feitas

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def busca(request):
    termo = request.GET.get('termo')
    contatos = Contato.objects.all()  # orm django - retorna lista com todos os dados
    paginator = Paginator(contatos, 10)  # limitando os contatos

    page = request.GET.get('page')  # vai pegar o parametro get page enviado pela url com o numero da pagina
    contatos = paginator.get_page(page)  # retona o objeto contato mais indice de paginas feitas

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })




def contato(request, id_contato):
    contato = get_object_or_404(Contato, id=id_contato)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/contato.html', {
        'contato': contato
    })


