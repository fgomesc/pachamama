from django.urls import path
from .views import \
    ContasAPagarList,\
    ContasAPagarEdit,\
    ContasAPagarDelete,\
    ContasAPagarCreate, \
    EnviarContasaPagarAprovacao, \
    AprovarContasAParagarList1,\
    AprovarContasAPagar1, \
    RecusarContaAPagar1, \
    AprovarContasAParagarList2,\
    AprovarContasAPagar2, \
    RecusarContaAPagar2, \
    EnviarParaPagamentoContasAPagarEdit, \
    EnviarPgamento, \
    EvolucaoFiscalList, \
    EvolucaoFiscalEdit, \
    EvolucaoFiscalEvoluir, \
    MovimentodoDiaList,\
    MovimentodoDiaEdit, \
    MovimentodoDiaEvolucao, \
    MovimentodoDiaRetornar, \
    MovimentodoDiaBaixar, \
    CancelarBaixa



urlpatterns = [
    path('', ContasAPagarList.as_view(), name='list_contas_a_pagar'),
    path('editar/<int:pk>/', ContasAPagarEdit.as_view(), name='edit_contas_a_pagar'),
    path('delete/<int:pk>/', ContasAPagarDelete.as_view(), name='delete_contas_a_pagar'),
    path('novo/', ContasAPagarCreate.as_view(), name='create_cadastro_estouro'),
    path('enviar-aprovacao-contas-a-pagar/<int:pk>', EnviarContasaPagarAprovacao.as_view(), name='enviar_contas_a_pagar_aprovacao'),
    path('aprovar-contas-a-pagar1', AprovarContasAParagarList1.as_view(), name='list_aprovar_contas_a_pagar'),
    path('editar-contas-a-pagar1/<int:pk>/', AprovarContasAPagar1.as_view(), name='aprovar_contas_a_pagar'),
    path('recusar-contas-a-pagar1/<int:pk>/', RecusarContaAPagar1.as_view(), name='recusar_contas_a_pagar'),
    path('aprovar-estouro2', AprovarContasAParagarList2.as_view(), name='list_aprovar_contas_a_pagar2'),
    path('recusar-estouro2/<int:pk>/', AprovarContasAPagar2.as_view(), name='aprovar_contas_a_pagar2'),
    path('editar-aprovador2/<int:pk>/', RecusarContaAPagar2.as_view(), name='recusar_contas_a_pagar2'),
    path('editar-enviar-para-pagamento/<int:pk>/', EnviarParaPagamentoContasAPagarEdit.as_view(), name='anexar_boleto_contas_a_receber'),
    path('enviar-enviar-para-pagamento/<int:pk>/', EnviarPgamento.as_view(), name='enviar_pagamento_contas_a_receber'),
    path('evolucao-fiscal', EvolucaoFiscalList.as_view(), name='list_evolucao_fiscal'),
    path('editar-fiscal/<int:pk>/', EvolucaoFiscalEdit.as_view(), name='edit_evolucao_fiscal'),
    path('enviar-fiscal-pagamento/<int:pk>', EvolucaoFiscalEvoluir.as_view(), name='enviar_fiscal_para_financeiro'),
    path('movimento-diario-contas-a-pagar', MovimentodoDiaList.as_view(), name='list_movimento_do_dia'),
    path('editar-movimento-diario-contas-a-pagar/<int:pk>/', MovimentodoDiaEdit.as_view(), name='edit_movimento_do_dia'),
    path('enviar-mov-do-dia-contas-a-pagar/<int:pk>', MovimentodoDiaEvolucao.as_view(), name='enviar_movimento_contas'),
    path('retornar-status-mov-do-dia-contas-a-pagar/<int:pk>', MovimentodoDiaRetornar.as_view(), name='retornar_movimento_contas'),
    path('baixar-status-mov-do-dia-contas-a-pagar/<int:pk>', MovimentodoDiaBaixar.as_view(), name='baixar_movimento_contas'),
    path('cancelar-baixa-mov-do-dia-contas-a-pagar/<int:pk>', CancelarBaixa.as_view(), name='cancelar_baixa'),

]
