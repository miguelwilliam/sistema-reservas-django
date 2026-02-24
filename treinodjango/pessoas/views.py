from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def home(request):
    return render(request, 'pessoas/index.html')

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