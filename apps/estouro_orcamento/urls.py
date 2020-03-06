from django.urls import path
from .views import CadastroEstouroList, CadastroEstouroEdit, CadastroEstouroDelete, CadastroEstouroCreate, \
    load_naturezas, EnviarEstouroAprovacao, AprovarEstouroListOrcamento1, AprovarEstouroOrcamento1, \
    RecusarEstouroOrcamento1

urlpatterns = [
    path('', CadastroEstouroList.as_view(), name='list_cadastro_estouro'),
    path('editar/<int:pk>/', CadastroEstouroEdit.as_view(), name='edit_cadastro_estouro'),
    path('delete/<int:pk>/', CadastroEstouroDelete.as_view(), name='delete_cadastro_estouro'),
    path('novo/', CadastroEstouroCreate.as_view(), name='create_cadastro_estouro'),
    path('enviar-aprovacao-estouro/<int:pk>', EnviarEstouroAprovacao.as_view(), name='enviar_estouro_aprovacao'),
    path('ajax/load-naturezas/', load_naturezas, name='ajax_load_naturezas'),
    path('aprovar-estouro1', AprovarEstouroListOrcamento1.as_view(), name='list_aprovar_estouro'),
    path('recusar-estouro1/<int:pk>/', RecusarEstouroOrcamento1.as_view(), name='recusar_estouro_orcamento'),
    path('editar-aprovador/<int:pk>/', AprovarEstouroOrcamento1.as_view(), name='aprovar_estouro_orcamento'),

]
