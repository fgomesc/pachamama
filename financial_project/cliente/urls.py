from django.urls import path
from .views import ClienteList, ClienteCreate, ClienteEdit, ClienteDelete, ExportarClienteCSV, ExportarClienteExcel


urlpatterns = [
    path('', ClienteList.as_view(), name='list_cliente'),
    path('editar/<int:pk>/', ClienteEdit.as_view(), name='edit_cliente'),
    path('delete/<int:pk>/', ClienteDelete.as_view(), name='delete_cliente'),
    path('novo/', ClienteCreate.as_view(), name='create_cliente'),
    path('exportar-csv/', ExportarClienteCSV.as_view(), name='cliente_exportar_csv'),
    path('exportar-xls/', ExportarClienteExcel.as_view(), name='cliente_exportar_xls'),
]