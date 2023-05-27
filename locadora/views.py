from django.shortcuts import render
from .models import Locacao, Filme

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista_filmes(request):
    filmes = Filme.objects.all()
    context = {
        'filmes':filmes
    }
    return render(request, 'filmes.html', context)

def lista_locacao(request):
    locacoes = Locacao.objects.all()
    context = {
        'locacoes':locacoes
    }
    return render(request,'locacao.html', context)