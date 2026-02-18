from django import forms
from . import models

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = models.Emprestimo
        fields = ['data_hora_devolucao']
    
    pessoa_id = forms.ModelChoiceField(queryset=models.Pessoa.objects.all(), empty_label='Selecionar pessoa', to_field_name='nome', label='Pessoa responsável')
    item_id = forms.ModelChoiceField(queryset=models.Item.objects.all(), empty_label='Selecionar item', to_field_name='nome', label='Item emprestado')