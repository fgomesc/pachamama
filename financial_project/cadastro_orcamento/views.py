from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from financial_project.centro_de_custo.models import CentroDeCusto
from financial_project.usuario.models import Usuario



def get_centros_usuario(id):
    return Usuario.objects.filter(user__id=id).first().centrodecusto_usuario.all()



class OrcamentoGlobalList(LoginRequiredMixin, ListView):
    model = CentroDeCusto
    template_name = 'cadastro_orcamento/orcamentoglobal_list.html'

    def get_queryset(self):
        return get_centros_usuario(self.request.user.id)



class NaturezasPorCentro(LoginRequiredMixin, TemplateView):
    template_name = 'cadastro_orcamento/natureza_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        centro_id = self.kwargs.get('id', 0)
        centro = CentroDeCusto.objects.get(id = centro_id)
        context.update({
            'centro' : centro,
            'naturezas' : centro.vinculo_natureza.all()
        })

        return context