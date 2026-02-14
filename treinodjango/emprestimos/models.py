from django.db import models
from itens.models import Item
from pessoas.models import Pessoa

# Create your models here.
class Emprestimo(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    pessoa_id = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_hora = models.DateTimeField("Data e Hora do Empréstimo", auto_now=True)