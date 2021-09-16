from apps.contas_a_pagar.models import ContaAPagar
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = ContaAPagar
        fields = ['cliente_contas_a_pagar',
                  'data_pagamento_contas_a_pagar',
                  'data_pagamento_contas_a_pagar', ]