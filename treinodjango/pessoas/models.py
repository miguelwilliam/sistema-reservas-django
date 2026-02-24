from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=255)
    numero = models.CharField('Número de celular (DDD e números apenas)', max_length=11)

    def __str__(self):
        return self.nome