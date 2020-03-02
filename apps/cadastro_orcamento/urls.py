from django.urls import path
from .views import CadastroOrcamentoList, CadastroOrcamentoEdit, CadastroOrcamentoDelete, CadastroOrcamentoCreate, \
    load_naturezas, OrcamentoGlobalList, NaturezasPorCentro

urlpatterns = [
    path('', CadastroOrcamentoList.as_view(), name='list_cadastro_orcamento'),
    path('editar/<int:pk>/', CadastroOrcamentoEdit.as_view(), name='edit_cadastro_orcamento'),
    path('delete/<int:pk>/', CadastroOrcamentoDelete.as_view(), name='delete_cadastro_orcamento'),
    path('novo/', CadastroOrcamentoCreate.as_view(), name='create_cadastro_orcamento'),
    path('ajax/load-naturezas/', load_naturezas, name='ajax_load_naturezas'),
    path('orcamentoglobal/', OrcamentoGlobalList.as_view(), name='list_orcamentoglobal'),
    path('<int:id>/naturezas/', NaturezasPorCentro.as_view(), name='naturezas_orcamentarias')
]