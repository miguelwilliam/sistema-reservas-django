from django import forms
from django.apps import apps
from . import models
from itens.models import Item

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = models.Emprestimo
        fields = ['pessoa', 'item']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['item'].queryset = Item.objects.filter(atualmente_emprestado = False)
