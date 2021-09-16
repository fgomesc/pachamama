from django.urls import path
from financial_project.produto.views import ProdutoList, ProdutoCreate, ProdutoEdit

urlpatterns = [
    path('', ProdutoList.as_view(), name='list_produto'),
    path('novo/', ProdutoCreate.as_view(), name='create_produto'),
    path('editar/<int:pk>/', ProdutoEdit.as_view(), name='edit_produto'),
]