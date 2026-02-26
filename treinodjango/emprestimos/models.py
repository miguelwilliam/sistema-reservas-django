from django.db import models
from itens.models import Item
from pessoas.models import Pessoa

# Create your models here.
class Emprestimo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_hora_emprestimo = models.DateTimeField("Data e Hora do Empréstimo", auto_now_add=True)
    data_hora_devolucao = models.DateTimeField("Data e Hora da Devolução", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: # SE O EMPRESTIMO AINDA NÃO TIVER SIDO SALVO   
            self.item.atualmente_emprestado = True
            self.item.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.item.atualmente_emprestado = False
        self.item.save()

        super().delete(*args, **kwargs)