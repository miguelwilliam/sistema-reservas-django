from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import forms
from .models import Emprestimo

# Create your views here.
def home(request):
    emprestimos = Emprestimo.objects.all().order_by('-data_hora_emprestimo')
    context = {'emprestimos': emprestimos}
    return render(request, 'emprestimos/index.html', context)

def novo(request):
    form = forms.EmprestimoForm

    if request.method == 'POST':
        form = forms.EmprestimoForm(request.POST)
        #print(request.POST)
        if form.is_valid():
            # O CÓDIGO ABAIXO FOI MOVIDO PARA O 'MODELS.PY'
            # Item = apps.get_model('itens', 'Item')
            # Item.objects.filter(id = request.POST['item']).update(atualmente_emprestado = True)

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

def devolucao(request, id):
    try:
        emprestimo = get_object_or_404(Emprestimo, id=id)
        emprestimo.item.atualmente_emprestado = False
        emprestimo.data_hora_devolucao = timezone.localtime(timezone.now())
        print(timezone.localtime(timezone.now()))

        emprestimo.item.save()
        emprestimo.save()
        print('DEVOLUÇÃO CADASTRADA COM SUCESSO')
        return redirect('emprestimos:home')
    except:
        print('ERRO AO CADASTRAR DEVOLUÇÃO')
        return redirect('emprestimos:home')