from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from financial_project.centro_de_custo.models import CentroDeCusto
from financial_project.perfil.models import Perfil
from financial_project.permissao.models import Permissao


class Usuario(models.Model):
    primeiro_nome = models.CharField(max_length=70)
    ultimo_nome = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    centrodecusto_usuario = models.ManyToManyField(CentroDeCusto)
    perfil_usuario = models.ForeignKey(Perfil, on_delete=models.PROTECT, null=True, blank=True)
    permissao_usuario = models.ForeignKey(Permissao, on_delete=models.PROTECT, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('list_usuario')


    def __str__(self):
        return self.primeiro_nome
