from django.urls import path
from .views import PermissaoList, PermissaoEdit, PermissaoDelete, PermissaoCreate, ExportarPermissaoCSV, ExportarPermissaoExcel

urlpatterns = [
    path('', PermissaoList.as_view(), name='list_permissao'),
    path('editar/<int:pk>/', PermissaoEdit.as_view(), name='edit_permissao'),
    path('delete/<int:pk>/', PermissaoDelete.as_view(), name='delete_permissao'),
    path('novo/', PermissaoCreate.as_view(), name='create_permissao'),
    path('exportar-csv/', ExportarPermissaoCSV.as_view(), name='permissao_exportar_csv'),
    path('exportar-xls/', ExportarPermissaoExcel.as_view(), name='permissao_exportar_xls'),
]