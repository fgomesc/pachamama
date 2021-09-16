from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from financial_project.produto.models import Produto
from django.db.models import Q


class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto

    def get_queryset(self):
        queryset = super(ProdutoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(produto__icontains=search) |
                Q(ncm__icontains=search)
            )
        return queryset


class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['importado', 'ncm', 'produto', 'preco', 'estoque', 'estoque_minimo', 'data', 'categoria']

class ProdutoEdit(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['importado', 'ncm', 'produto', 'preco', 'estoque', 'estoque_minimo', 'data', 'categoria']