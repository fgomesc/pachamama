from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.cadastro_orcamento.models import CadastroOrcamento
from apps.centro_de_custo.models import CentroDeCusto
from apps.usuario.models import Usuario
from .forms import CadastroOrcamentoForm


class CadastroOrcamentoList(LoginRequiredMixin, ListView):
    model = CadastroOrcamento

    def get_queryset(self):
        print(self.request.user.pk)
        centros = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return CadastroOrcamento.objects.filter(cc_cadastro_orcamento__in=centros)


class CadastroOrcamentoEdit(LoginRequiredMixin, UpdateView):
    model = CadastroOrcamento
    form_class = CadastroOrcamentoForm

    def get_form_kwargs(self):
        kwargs = super(CadastroOrcamentoEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class CadastroOrcamentoDelete(LoginRequiredMixin, DeleteView):
    model = CadastroOrcamento
    success_url = reverse_lazy('list_cadastro_orcamento')

class CadastroOrcamentoCreate(LoginRequiredMixin, CreateView):
    model = CadastroOrcamento
    form_class = CadastroOrcamentoForm

    def get_form_kwargs(self):
        kwargs = super(CadastroOrcamentoCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


def load_naturezas(request):
    centro_id = request.GET.get('centro')
    centro = CentroDeCusto.objects.filter(pk=centro_id).first()
    naturezas = centro.vinculo_natureza.all()

    return render(request, 'naturezas_list_options.html', {'naturezas' : naturezas})



def get_centros_usuario(id):
    return Usuario.objects.filter(user__id = id).first().centrodecusto_usuario.all()



class OrcamentoGlobalList(LoginRequiredMixin, ListView):
    model = CentroDeCusto
    template_name = 'orcamentoglobal_list.html'

    def get_queryset(self):
        return get_centros_usuario(self.request.user.id)



class NaturezasPorCentro(LoginRequiredMixin, TemplateView):
    template_name = 'natureza_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        centro_id = self.kwargs.get('id', 0)
        centro = CentroDeCusto.objects.get(id = centro_id)
        context.update({
            'centro' : centro,
            'naturezas' : centro.vinculo_natureza.all()
        })

        return context