from django.urls import path
from .views import OrcamentoGlobalList, NaturezasPorCentro

urlpatterns = [
    path('orcamentoglobal/', OrcamentoGlobalList.as_view(), name='list_orcamentoglobal'),
    path('<int:id>/naturezas/', NaturezasPorCentro.as_view(), name='naturezas_orcamentarias'),
]