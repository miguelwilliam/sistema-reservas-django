from django.shortcuts import render, redirect
from . import forms
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
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