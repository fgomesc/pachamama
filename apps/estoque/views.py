from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from apps.estoque.models import Estoque
from django.db.models import Q


class EstoqueList(LoginRequiredMixin, ListView):
    model = Estoque

    def get_queryset(self):
        queryset = super(EstoqueList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(produto__icontains=search) |
                Q(ncm__icontains=search)
            )
        return queryset

class EstoqueDetail(DetailView):
    model = Estoque