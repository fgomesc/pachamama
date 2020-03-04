from django.forms import ModelForm
from .models import CadastroEstouroOrcamento



class CadastroEstouroForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CadastroEstouroForm, self).__init__(*args, **kwargs)
        self.fields['cc_cadastro_orcamento'].queryset = user.usuario.centrodecusto_usuario.all()



    class Meta:
        model = CadastroEstouroOrcamento
        fields = ['cc_cadastro_orcamento', 'no_cadastro_orcamento', 'valor_cadastro_orcamento', 'data_cadastro_orcamento', 'obs_cadastro_orcamento', 'aprovacao', 'status']

