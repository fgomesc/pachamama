from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from financial_project.centro_de_custo.models import CentroDeCusto


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=140)
    centro_de_custo_cliente = models.ForeignKey(CentroDeCusto, on_delete=models.PROTECT, null=True, blank=True)
    user_cliente = models.OneToOneField(User, on_delete=models.PROTECT)


    def get_absolute_url(self):
        return reverse('list_cliente')


    def __str__(self):
        return self.nome_cliente