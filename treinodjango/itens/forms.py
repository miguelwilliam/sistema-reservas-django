from django import forms
from itens.models import Item, Categoria

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'desc', 'categoria_id']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']