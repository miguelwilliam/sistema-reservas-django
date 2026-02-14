from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'itens/index.html')

def novo_item(request):
    return HttpResponse('formulário de criar novo item aqui')

def nova_categoria(request):
    return HttpResponse('Formulário de criar nova categoria')