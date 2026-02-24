from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def home(request):
    return render(request, 'emprestimos/index.html')

def novo(request):
    form = forms.EmprestimoForm

    if request == 'POST':
        form = forms.EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            print('EMPRESTIMO SALVO COM SUCESSO')

            return redirect('emprestimos:home')
    
    context = {'form': form}
    return render(request, 'emprestimos/novo.html', context)