from django.db import models
from django.urls import reverse
from apps.centro_de_custo.models import CentroDeCusto
from apps.natureza_orcamentaria.models import NaturezaOrcamentaria

class CadastroEstouroOrcamento(models.Model):
    STATUS_CHOICES = (
        ('Criado', 'Criado'),
        ('Em Aprovação', 'Em Aprovação'),
        ('Aprovado', 'Aprovado'),
    )

    cc_cadastro_orcamento = models.ForeignKey(CentroDeCusto, on_delete=models.PROTECT, null=True, blank=True)
    no_cadastro_orcamento = models.ForeignKey(NaturezaOrcamentaria, on_delete=models.PROTECT, null=True, blank=True)
    valor_cadastro_orcamento = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro_orcamento = models.DateField(null=True, blank=True)
    obs_cadastro_orcamento = models.CharField(max_length=1000)
    aprovacao = models.BooleanField(verbose_name='Aprovação', default=False)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES, default='Criado')




    def get_absolute_url(self):
        return reverse('list_cadastro_estouro')


    def __str__(self):
        return self.obs_cadastro_orcamento


