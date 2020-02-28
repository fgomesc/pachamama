from django.urls import path
from .views import CentrodecustoList, CentrodecustoEdit, CentrodecustoDelete, CentrodecustoCreate, ExportarCentrodeCustoCSV, ExportarCentrodeCustoExcel

urlpatterns = [
    path('', CentrodecustoList.as_view(), name='list_centrodecusto'),
    path('editar/<int:pk>/', CentrodecustoEdit.as_view(), name='edit_centrodecusto'),
    path('delete/<int:pk>/', CentrodecustoDelete.as_view(), name='delete_centrodecusto'),
    path('novo/', CentrodecustoCreate.as_view(), name='create_centrodecusto'),
    path('exportar-csv/', ExportarCentrodeCustoCSV.as_view(), name='centrodecusto_exportar_csv'),
    path('exportar-xls/', ExportarCentrodeCustoExcel.as_view(), name='centrodecusto_exportar_xls'),

]