from django.db import models
from django.urls import reverse
from apps.centro_de_custo.models import CentroDeCusto
from apps.natureza_orcamentaria.models import NaturezaOrcamentaria

class ContaAPagar(models.Model):
    STATUS_CHOICES = (('C', 'Criado'),
                      ('A1', 'Aprovação 1'),
                      ('A2', 'Aprovação 2'),
                      ('AP', 'Aprovado'),
                      ('EF', 'Evolução Fiscal'),
                      ('EFF', 'Eviar Financeiro'),
                      ('MOV', 'Movimento do Dia'),
                      ('BX', 'Baixado'))

    cliente_contas_a_pagar = models.ForeignKey(CentroDeCusto, on_delete=models.PROTECT, null=True, blank=True)
    caso_contas_a_pagar = models.CharField(max_length=100)
    data_input_contas_a_pagar = models.DateField(auto_now=True)
    data_pagamento_contas_a_pagar = models.DateField(null=True, blank=True)
    natureza_contas_a_pagar = models.ForeignKey(NaturezaOrcamentaria, on_delete=models.PROTECT, null=True, blank=True)
    correspondente_contas_a_pagar = models.CharField(max_length=100)
    fornecedor_contas_a_pagar = models.CharField(max_length=100)
    historico_contas_a_pagar = models.TextField(max_length=1000000)
    valor_contas_a_pagar = models.DecimalField(max_digits=100, decimal_places=2)
    conta_debito_contas_a_pagar = models.CharField(max_length=100)
    banco_beneficiario_contas_a_pagar = models.CharField(max_length=100, blank=True)
    ag_beneficiario_contas_a_pagar = models.CharField(max_length=100, blank=True)
    cc_beneficiario_contas_a_pagar = models.CharField(max_length=100, blank=True)
    anexo_boleto_contas_a_pagar = models.FileField(upload_to='anexo_boleto/', null=True, blank=True)
    anexo_comprovante_contas_a_pagar = models.FileField(upload_to='anexo_comprovante/', null=True, blank=True)
    iss_contas_a_pagar = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    pis_contas_a_pagar = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    cofins_contas_a_pagar = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    css_contas_a_pagar = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    ir_contas_a_pagar = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    status_contas_a_pagar = models.CharField(max_length=3, choices=STATUS_CHOICES, default='C', blank=False, null=False)


    def get_absolute_url(self):
        return reverse('list_contas_a_pagar')

    def __str__(self):
        return self.historico_contas_a_pagar


