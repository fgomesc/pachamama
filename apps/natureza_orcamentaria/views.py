import csv

import xlwt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import NaturezaOrcamentaria
from django.views import View


class NaturezaList(LoginRequiredMixin, ListView):
    model = NaturezaOrcamentaria


class NaturezaEdit(LoginRequiredMixin, UpdateView):
    model = NaturezaOrcamentaria
    fields = ['numero_natureza', 'nome_natureza', 'natureza_orcamento']


class NaturezaDelete(LoginRequiredMixin, DeleteView):
    model = NaturezaOrcamentaria
    success_url = reverse_lazy('list_natureza')

class NaturezaCreate(LoginRequiredMixin, CreateView):
    model = NaturezaOrcamentaria
    fields = ['numero_natureza', 'nome_natureza', 'natureza_orcamento']


class ExportarNaturezaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        dados = NaturezaOrcamentaria.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Numero Natureza', 'Nome Natureza', 'Natureza Orçamentária'])
        for natureza in dados:
            writer.writerow([natureza.id, natureza.numero_natureza, natureza.nome_natureza, natureza.natureza_orcamento])

        return response

class ExportarNaturezaExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='urf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Numero Natureza', 'Nome Natureza', 'Natureza Orçamentária']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        dados = NaturezaOrcamentaria.objects.all()

        row_num = 1

        for natureza in dados:
            ws.write(row_num, 0, natureza.id, font_style)
            ws.write(row_num, 1, natureza.numero_natureza, font_style)
            ws.write(row_num, 2, natureza.nome_natureza, font_style)
            ws.write(row_num, 3, natureza.natureza_orcamento, font_style)

            row_num += 1

        wb.save(response)
        return response