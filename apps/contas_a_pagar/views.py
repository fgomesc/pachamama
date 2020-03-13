from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.contas_a_pagar.forms import CadastroContasAPagarForm
from .models import ContaAPagar
from apps.usuario.models import Usuario




""" <<<<<< Contas a Pagar - Cadastro

Criando Lançamento de contas a pagar

Parte aonde o usuário lançador ira criar os lançamentos de contas a pagar

"""



class ContasAPagarList(LoginRequiredMixin, ListView):
    model = ContaAPagar

    def get_queryset(self):
        print(self.request.user.pk)
        centros = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return ContaAPagar.objects.filter(cliente_contas_a_pagar__in=centros)

class ContasAPagarEdit(PermissionRequiredMixin, UpdateView):
    model = ContaAPagar
    form_class = CadastroContasAPagarForm
    permission_required = 'global_permissions.cadastro_contas_a_pagar'

    def get_form_kwargs(self):
        kwargs = super(ContasAPagarEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class ContasAPagarDelete(PermissionRequiredMixin, DeleteView):
    model = ContaAPagar
    success_url = reverse_lazy('list_contas_a_pagar')
    permission_required = 'global_permissions.cadastro_contas_a_pagar'



class ContasAPagarCreate(PermissionRequiredMixin, CreateView):
    model = ContaAPagar
    form_class = CadastroContasAPagarForm
    permission_required = 'global_permissions.cadastro_contas_a_pagar'

    def get_form_kwargs(self):
        kwargs = super(ContasAPagarCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class EnviarContasaPagarAprovacao(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.cadastro_contas_a_pagar'


    def get(self, *args, **kwargs):
        status_contasapagar = ContaAPagar.objects.get(id=kwargs['pk'])
        status_contasapagar.status_contas_a_pagar = 'A1'
        status_contasapagar.save()

        return HttpResponseRedirect(reverse_lazy('list_contas_a_pagar'))


""" <<<<<< Contas a Pagar - Aprovação 1 

Aprovando Contas a Pagar pelo primeiro aprovador

Parte aonde o primeiro aprovador ira realizar a aprovação

"""

class AprovarContasAParagarList1(LoginRequiredMixin, ListView):
    model = ContaAPagar
    form_class = CadastroContasAPagarForm
    template_name = 'contas_a_pagar/aprovarcontasapagar1_list.html'


    def get_queryset(self):
        print(self.request.user.pk)
        contas = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return ContaAPagar.objects.filter(status_contas_a_pagar='A1', cliente_contas_a_pagar__in=contas)


class AprovarContasAPagar1(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.aprovacao1_estouro_orcamento'

    def get(self, *args, **kwargs):
        status_contasapagarap1 = ContaAPagar.objects.get(id=kwargs['pk'])
        status_contasapagarap1.status_contas_a_pagar = 'A2'
        status_contasapagarap1.save()

        return HttpResponseRedirect(reverse_lazy('list_aprovar_contas_a_pagar'))


class RecusarContaAPagar1(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.aprovacao1_estouro_orcamento'

    def get(self, *args, **kwargs):
        status_contasapagarap1 = ContaAPagar.objects.get(id=kwargs['pk'])
        status_contasapagarap1.status_contas_a_pagar = 'C'
        status_contasapagarap1.save()

        return HttpResponseRedirect(reverse_lazy('list_aprovar_contas_a_pagar'))


""" <<<<<< Contas a Pagar - Aprovação 2

Aprovando Contas a Pagar pelo segundo aprovador

Parte aonde o segundo aprovador ira realizar a aprovação

"""

class AprovarContasAParagarList2(LoginRequiredMixin, ListView):
    model = ContaAPagar
    form_class = CadastroContasAPagarForm
    template_name = 'contas_a_pagar/aprovarcontasapagar2_list.html'


    def get_queryset(self):
        print(self.request.user.pk)
        contas = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return ContaAPagar.objects.filter(status_contas_a_pagar='A2', cliente_contas_a_pagar__in=contas)


class AprovarContasAPagar2(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.aprovacao2_estouro_orcamento'

    def get(self, *args, **kwargs):
        status_contasapagarap1 = ContaAPagar.objects.get(id=kwargs['pk'])
        status_contasapagarap1.status_contas_a_pagar = 'AP'
        status_contasapagarap1.save()

        return HttpResponseRedirect(reverse_lazy('list_aprovar_contas_a_pagar2'))


class RecusarContaAPagar2(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.aprovacao2_estouro_orcamento'

    def get(self, *args, **kwargs):
        status_contasapagarap1 = ContaAPagar.objects.get(id=kwargs['pk'])
        status_contasapagarap1.status_contas_a_pagar = 'C'
        status_contasapagarap1.save()

        return HttpResponseRedirect(reverse_lazy('list_aprovar_contas_a_pagar2'))




""" <<<<<< Contas a Pagar - Envio Para Pagamento

Enviando o pagamento para o financeiro

Parte aonde o lançador envia o lançamnto para o financeiro realizar o pagamento. 

"""

class EnviarParaPagamentoContasAPagarEdit(PermissionRequiredMixin, UpdateView):
    model = ContaAPagar
    fields = ['anexo_boleto_contas_a_pagar']
    permission_required = 'global_permissions.cadastro_contas_a_pagar'


class EnviarPgamento(PermissionRequiredMixin, View):
    permission_required = 'global_permissions.cadastro_contas_a_pagar'

    def get(self, *args, **kwargs):
        status_contasapagarap1 = ContaAPagar.objects.get(id=kwargs['pk'])
        status_contasapagarap1.status_contas_a_pagar = 'PG'
        status_contasapagarap1.save()

        return HttpResponseRedirect(reverse_lazy('list_contas_a_pagar'))
