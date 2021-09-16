from django.db import models
from django.urls import reverse


class NaturezaOrcamentaria(models.Model):
    numero_natureza = models.CharField(max_length=70)
    nome_natureza = models.CharField(max_length=70)
    natureza_orcamento = models.CharField(max_length=140)



    def get_absolute_url(self):
        return reverse('list_natureza')


    def __str__(self):
        return self.natureza_orcamento