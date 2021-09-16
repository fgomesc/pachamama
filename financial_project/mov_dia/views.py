from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MovdoDia


class MovDiaList(LoginRequiredMixin, ListView):
    model = MovdoDia

class MovDiaEdit(LoginRequiredMixin, UpdateView):
    model = MovdoDia
    fields = ['cliente', 'razao_social', 'identificacao', 'sav', 'data_prov', 'valor_prov', 'conta_corrente', 'codigo_de_barras', 'banco_dep', 'ag_dep', 'conta_dep', 'anexo']

class MovDiaDelete(LoginRequiredMixin, DeleteView):
    model = MovdoDia
    success_url = reverse_lazy('list_mov_dia')


class MovDiaCreate(LoginRequiredMixin, CreateView):
    model = MovdoDia
    fields = ['cliente', 'razao_social', 'identificacao', 'sav', 'data_prov', 'valor_prov', 'conta_corrente', 'codigo_de_barras', 'banco_dep', 'ag_dep', 'conta_dep', 'anexo']

