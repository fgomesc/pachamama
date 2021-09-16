from django.db import models
from django.urls import reverse


class MovdoDia(models.Model):
    cliente = models.CharField(max_length=1000)
    razao_social = models.CharField(max_length=1000)
    caso = models.CharField(max_length=1000)
    identificacao = models.CharField(max_length=1000)
    sav = models.CharField(max_length=1000)
    data_prov = models.DateField()
    adv = models.CharField(max_length=1000)
    valor_prov = models.CharField(max_length=1000)
    conta_corrente = models.CharField(max_length=1000)
    codigo_de_barras = models.CharField(max_length=1000)
    banco_dep = models.CharField(max_length=1000)
    ag_dep = models.CharField(max_length=1000)
    conta_dep = models.CharField(max_length=1000)
    anexo = models.FileField()

    def get_absolute_url(self):
        return reverse('list_mov_dia')

    def __str__(self):
        return self.cliente
