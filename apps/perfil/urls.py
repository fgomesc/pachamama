from django.urls import path
from .views import PerfilList, PerfilEdit, PerfilDelete, PerfilCreate, ExportarPerfilCSV, ExportarPerfilExcel

urlpatterns = [
    path('', PerfilList.as_view(), name='list_perfil'),
    path('editar/<int:pk>/', PerfilEdit.as_view(), name='edit_perfil'),
    path('delete/<int:pk>/', PerfilDelete.as_view(), name='delete_perfil'),
    path('novo/', PerfilCreate.as_view(), name='create_perfil'),
    path('exportar-csv/', ExportarPerfilCSV.as_view(), name='perfil_exportar_csv'),
    path('exportar-xls/', ExportarPerfilExcel.as_view(), name='perfil_exportar_xls'),

]