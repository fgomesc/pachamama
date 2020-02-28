from django.forms import ModelForm
from .models import CadastroOrcamento



class CadastroOrcamentoForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CadastroOrcamentoForm, self).__init__(*args, **kwargs)
        self.fields['cc_cadastro_orcamento'].queryset = user.usuario.centrodecusto_usuario.all()



    class Meta:
        model = CadastroOrcamento
        fields = ['cc_cadastro_orcamento', 'no_cadastro_orcamento', 'no_cadastro_orcamento', 'valor_cadastro_orcamento', 'data_cadastro_orcamento', 'obs_cadastro_orcamento']
