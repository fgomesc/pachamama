from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views import View
from apps.centro_de_custo.models import CentroDeCusto
from apps.usuario.models import Usuario
from .forms import CadastroEstouroOrcamento, CadastroEstouroForm



""" <<<<<< Estouro de Verba - Cadastro

Criando Estouro de Orçamento

Parte aonde o usuário lançador ira criar os estouros de orçamento

"""

class CadastroEstouroList(LoginRequiredMixin, ListView):
    model = CadastroEstouroOrcamento

    def get_queryset(self):
        print(self.request.user.pk)
        centros = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return CadastroEstouroOrcamento.objects.filter(cc_cadastro_orcamento__in=centros)



class CadastroEstouroEdit(PermissionRequiredMixin, UpdateView):
    model = CadastroEstouroOrcamento
    form_class = CadastroEstouroForm
    permission_required = 'global_permissions.cadastro_estouro_orcamento'

    def get_form_kwargs(self):
        kwargs = super(CadastroEstouroEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class CadastroEstouroDelete(PermissionRequiredMixin, DeleteView):
    model = CadastroEstouroOrcamento
    success_url = reverse_lazy('list_cadastro_estouro')
    permission_required = 'global_permissions.cadastro_estouro_orcamento'



class CadastroEstouroCreate(PermissionRequiredMixin, CreateView):
    model = CadastroEstouroOrcamento
    form_class = CadastroEstouroForm
    permission_required = 'global_permissions.cadastro_estouro_orcamento'

    def get_form_kwargs(self):
        kwargs = super(CadastroEstouroCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class EnviarEstouroAprovacao(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.cadastro_estouro_orcamento'


    def get(self, *args, **kwargs):
        status_estouro = CadastroEstouroOrcamento.objects.get(id=kwargs['pk'])
        status_estouro.status = 'A1'
        status_estouro.save()

        return HttpResponseRedirect(reverse_lazy('list_cadastro_estouro'))





""" <<<<<< Estouro de Verba - Aprovação 1 

Aprovando Estouro de Orçamento

Parte aonde o usuário aprova o estouro cadastrado pelo usuário lançador

"""


class AprovarEstouroListOrcamento1(LoginRequiredMixin, ListView):
    model = CadastroEstouroOrcamento
    form_class = CadastroEstouroForm
    template_name = 'estouro_orcamento/aprovarestouroorcamento_list.html'


    def get_queryset(self):
        print(self.request.user.pk)
        orcamentos = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return CadastroEstouroOrcamento.objects.filter(status='A1', cc_cadastro_orcamento__in=orcamentos)


class AprovarEstouroOrcamento1(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.aprovacao1_estouro_orcamento'

    def get(self, *args, **kwargs):
        status_estouro = CadastroEstouroOrcamento.objects.get(id=kwargs['pk'])
        status_estouro.status = 'A2'
        status_estouro.save()

        return HttpResponseRedirect(reverse_lazy('list_aprovar_estouro'))



class RecusarEstouroOrcamento1(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.aprovacao1_estouro_orcamento'


    def get(self, *args, **kwargs):
        status_estouro = CadastroEstouroOrcamento.objects.get(id=kwargs['pk'])
        status_estouro.status = 'C'
        status_estouro.save()



        return HttpResponseRedirect(reverse_lazy('list_aprovar_estouro'))



""" <<<<<< Estouro de Verba - Aprovação 2

Aprovando Estouro de Orçamento

Parte aonde o usuário aprova o estouro cadastrado pelo usuário lançador

"""


class AprovarEstouroListOrcamento2(LoginRequiredMixin, ListView):
    model = CadastroEstouroOrcamento
    form_class = CadastroEstouroForm
    template_name = 'estouro_orcamento/aprovarestouroorcamento2_list.html'


    def get_queryset(self):
        print(self.request.user.pk)
        orcamentos = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return CadastroEstouroOrcamento.objects.filter(status='A2', cc_cadastro_orcamento__in=orcamentos)


class AprovarEstouroOrcamento2(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.aprovacao2_estouro_orcamento'

    def get(self, *args, **kwargs):
        status_estouro = CadastroEstouroOrcamento.objects.get(id=kwargs['pk'])
        status_estouro.status = 'AP'
        status_estouro.save()

        return HttpResponseRedirect(reverse_lazy('list_aprovar_estouro2'))



class RecusarEstouroOrcamento2(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.aprovacao2_estouro_orcamento'


    def get(self, *args, **kwargs):
        status_estouro = CadastroEstouroOrcamento.objects.get(id=kwargs['pk'])
        status_estouro.status = 'C'
        status_estouro.save()



        return HttpResponseRedirect(reverse_lazy('list_aprovar_estouro2'))

"""


"""


def load_naturezas(request):
    centro_id = request.GET.get('centro')
    centro = CentroDeCusto.objects.filter(pk=centro_id).first()
    naturezas = centro.vinculo_natureza.all()

    return render(request, 'estouro_orcamento/naturezas_list_options.html', {'naturezas': naturezas})

