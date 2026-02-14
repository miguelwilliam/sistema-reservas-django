from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=255)

class Item(models.Model):
    nome = models.CharField('Nome',max_length=255)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    desc = models.CharField('Descrição', max_length=255)
    atualmente_emprestado = models.BooleanField('Está atualmente emprestado', default=False)