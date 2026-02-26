from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    context = {'pessoas': pessoas}
    return render(request, 'pessoas/index.html', context)

def nova(request):
    form = forms.PessoaForm

    if request.method == 'POST':
        form = forms.PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            print("PESSOA CADASTRADA COM SUCESSO!")

            return redirect('pessoas:home')
        
    context = {'form': form}
    return render(request, 'pessoas/nova.html', context)

def apagar(request, id):
    try:
        pessoa = get_object_or_404(Pessoa, id=id)
        pessoa.delete()

        print('CADASTRO APAGADO COM SUCESSO')
        return redirect('pessoas:home')
    except:
        print('OCORREU UM ERRO DURANTE O APAGAMENTO DO CADASTRO')
        return redirect('pessoas:home')