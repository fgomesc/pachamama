from django.forms import ModelForm
from .models import ContaAPagar



class CadastroContasAPagarForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CadastroContasAPagarForm, self).__init__(*args, **kwargs)
        self.fields['cliente_contas_a_pagar'].queryset = user.usuario.centrodecusto_usuario.all()



    class Meta:
        model = ContaAPagar
        fields = ['cliente_contas_a_pagar',
                  'natureza_contas_a_pagar',
                  'valor_contas_a_pagar',
                  'tipo_de_pagamento']


