from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Categoria, Item

# Create your views here.
def home(request):
    categorias = Categoria.objects.all().order_by('nome')
    itens = Item.objects.all().order_by('categoria')
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

            return redirect('itens:home')
    
    context = {'form': form}
    return render(request, 'itens/nova_categoria.html', context)

def apagar_item(request, id):
    try:
        item = get_object_or_404(Item, id=id)
        item.delete()

        print('ITEM APAGADO COM SUCESSO')
        return redirect('itens:home')
    
    except:
        print('ERRO AO APAGAR O ITEM')
        return redirect('itens:home')
    
def apagar_categoria(request, id):
    try:
        categoria = get_object_or_404(Categoria, id = id)
        categoria.delete()

        print('CATEGORIA APAGADA COM SUCESSO')
        return redirect('itens:home')
    
    except:
        print('ERRO AO APAGAR A CATEGORIA')
        return redirect('itens:home')

def editar_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if  form.is_valid():
            form.save()

            print('ITEM ATUALIZADO COM SUCESSO')
            return redirect('itens:home')
        
    form = forms.ItemForm(instance=item)

    context = {'form': form, 'tela_atual':'item'}
    return render(request, 'itens/editar.html', context)

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST, instance=categoria)
        if  form.is_valid():
            form.save()

            print('CATEGORIA ATUALIZADO COM SUCESSO')
            return redirect('itens:home')
        
    form = forms.CategoriaForm(instance=categoria)

    context = {'form': form, 'tela_atual':'categoria'}
    return render(request, 'itens/editar.html', context)