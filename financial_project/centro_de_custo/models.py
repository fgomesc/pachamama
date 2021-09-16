from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from financial_project.natureza_orcamentaria.models import NaturezaOrcamentaria


class CentroDeCusto(models.Model):
    numero_centro = models.CharField(max_length=70)
    nome_centro = models.CharField(max_length=70)
    centro_de_custo = models.CharField(max_length=70)
    user_respon = models.OneToOneField(User, on_delete=models.PROTECT)
    vinculo_natureza = models.ManyToManyField(NaturezaOrcamentaria)

    def get_absolute_url(self):
        return reverse('list_centrodecusto')


    def __str__(self):
        return self.centro_de_custo