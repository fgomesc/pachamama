from django.contrib import admin
from .models import MovdoDia




class MovDia(admin.ModelAdmin):
    list_display = ('cliente', 'razao_social', 'identificacao', 'sav', 'data_prov', 'valor_prov', 'conta_corrente', 'codigo_de_barras', 'banco_dep', 'ag_dep', 'conta_dep')
    search_fields = ('sav', 'valor_prov')
    list_editable = ('codigo_de_barras', 'banco_dep', 'ag_dep', 'conta_dep')


admin.site.register(MovdoDia, MovDia)