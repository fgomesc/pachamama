from django.urls import path
from .views import CadastroEstouroList, CadastroEstouroEdit, CadastroEstouroDelete, CadastroEstouroCreate, load_naturezas

urlpatterns = [
    path('', CadastroEstouroList.as_view(), name='list_cadastro_estouro'),
    path('editar/<int:pk>/', CadastroEstouroEdit.as_view(), name='edit_cadastro_estouro'),
    path('delete/<int:pk>/', CadastroEstouroDelete.as_view(), name='delete_cadastro_estouro'),
    path('novo/', CadastroEstouroCreate.as_view(), name='create_cadastro_estouro'),
    path('ajax/load-naturezas/', load_naturezas, name='ajax_load_naturezas'),

]

"""
path('aprovar-estouro', AprovarEstouroList.as_view(), name='list_aprovar_estouro'),
path('editar-aprovador/<int:pk>/', AprovadorOrcamentoEdit.as_view(), name='edit_aprovador_orcamento'),
"""