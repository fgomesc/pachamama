from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import ContaAPagar



class ContasAPagarList(ListView):
    model = ContaAPagar

class ContasAPagarEdit(UpdateView):
    model = ContaAPagar
    fields = ['cliente_contas_a_pagar',
              'caso_contas_a_pagar',
              'natureza_contas_a_pagar',
              'correspondente_contas_a_pagar',
              'historico_contas_a_pagar',
              'valor_contas_a_pagar',
              'conta_debito_contas_a_pagar',
              'banco_beneficiario_contas_a_pagar',
              'ag_beneficiario_contas_a_pagar',
              'cc_beneficiario_contas_a_pagar']


class ContasAPagarDelete(DeleteView):
    model = ContaAPagar
    success_url = reverse_lazy('list_contas_a_pagar')



class ContasAPagarCreate(CreateView):
    model = ContaAPagar
    fields = ['cliente_contas_a_pagar',
              'caso_contas_a_pagar',
              'natureza_contas_a_pagar',
              'correspondente_contas_a_pagar',
              'historico_contas_a_pagar',
              'valor_contas_a_pagar',
              'conta_debito_contas_a_pagar',
              'banco_beneficiario_contas_a_pagar',
              'ag_beneficiario_contas_a_pagar',
              'cc_beneficiario_contas_a_pagar']
