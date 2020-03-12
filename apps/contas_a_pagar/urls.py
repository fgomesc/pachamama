from django.urls import path
from .views import ContasAPagarList, ContasAPagarEdit, ContasAPagarDelete, ContasAPagarCreate


urlpatterns = [
    path('', ContasAPagarList.as_view(), name='list_contas_a_pagar'),
    path('editar/<int:pk>/', ContasAPagarEdit.as_view(), name='edit_contas_a_pagar'),
    path('delete/<int:pk>/', ContasAPagarDelete.as_view(), name='delete_contas_a_pagar'),
    path('novo/', ContasAPagarCreate.as_view(), name='create_cadastro_estouro'),

]
