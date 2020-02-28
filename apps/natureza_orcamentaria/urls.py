from django.urls import path
from .views import NaturezaList, NaturezaEdit, NaturezaDelete, NaturezaCreate, ExportarNaturezaCSV, ExportarNaturezaExcel

urlpatterns = [
    path('', NaturezaList.as_view(), name='list_natureza'),
    path('editar/<int:pk>/', NaturezaEdit.as_view(), name='edit_natureza'),
    path('delete/<int:pk>/', NaturezaDelete.as_view(), name='delete_natureza'),
    path('novo/', NaturezaCreate.as_view(), name='create_natureza'),
    path('exportar-csv/', ExportarNaturezaCSV.as_view(), name='natureza_exportar_csv'),
    path('exportar-xls/', ExportarNaturezaExcel.as_view(), name='natureza_exportar_xls'),


]