from django.shortcuts import render, redirect
from . import forms
from .models import Categoria, Item

# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    itens = Item.objects.all()
    context = {'categorias': categorias, 'itens': itens}
    return render(request, 'itens/index.html', context)

def novo_item(request):
    form = forms.ItemForm
    
    if request.method == 'POST':
        form = forms.ItemForm(request.POST)
        if form.is_valid():
            form.save()
            print('FORMULÁRIO SALVO COM SUCESSO')

            return redirect('itens:home')
    
    context = {'form': form}
    return render(request, 'itens/novo_item.html', context)

def nova_categoria(request):
    form = forms.CategoriaForm
    
    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            print('FORMULÁRIO SALVO COM SUCESSO')

            return render(request, 'itens/index.html')
    
    context = {'form': form}
    return render(request, 'itens/nova_categoria.html', context)