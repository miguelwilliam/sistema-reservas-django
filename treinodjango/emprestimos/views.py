from django.shortcuts import render, redirect
from django.apps import apps
from . import forms
from .models import Emprestimo

# Create your views here.
def home(request):
    emprestimos = Emprestimo.objects.all()
    context = {'emprestimos': emprestimos}
    return render(request, 'emprestimos/index.html', context)

def novo(request):
    form = forms.EmprestimoForm

    if request.method == 'POST':
        form = forms.EmprestimoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            Item = apps.get_model('itens', 'Item')
            Item.objects.filter(id = request.POST['item']).update(atualmente_emprestado = True)

            form.save()
            print('EMPRESTIMO SALVO COM SUCESSO')

            return redirect('emprestimos:home')
        else:
            print('FORMULÁRIO NÃO É VÁLIDO!')
    
    context = {'form': form}
    return render(request, 'emprestimos/novo.html', context)

def apagar(request, id):
    try:
        emprestimo = Emprestimo.objects.get(id=id)
        emprestimo.delete()

        print('EMPRESTIMO DELETADO COM SUCESSO')
        return redirect('emprestimos:home')
    except:
        print('ERRO AO DELETAR EMPRESTIMO')
        return redirect('emprestimos:home')