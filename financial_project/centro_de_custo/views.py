import csv

import xlwt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import CentroDeCusto
from django.views import View


class CentrodecustoList(LoginRequiredMixin, ListView):
    model = CentroDeCusto


class CentrodecustoEdit(LoginRequiredMixin, UpdateView):
    model = CentroDeCusto
    fields = ['numero_centro', 'nome_centro', 'centro_de_custo','user_respon', 'vinculo_natureza']

class CentrodecustoCreate(LoginRequiredMixin, CreateView):
    model = CentroDeCusto
    fields = ['numero_centro', 'nome_centro', 'centro_de_custo', 'user_respon', 'vinculo_natureza']

class CentrodecustoDelete(LoginRequiredMixin, DeleteView):
    model = CentroDeCusto
    success_url = reverse_lazy('list_centrodecusto')


class ExportarCentrodeCustoCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        dados = CentroDeCusto.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Numero Centro de Custo', 'Nome Centro de Custo', 'Centro de Custo', 'Usuário Responsável'])
        for centrodecusto in dados:
            writer.writerow([centrodecusto.id, centrodecusto.numero_centro, centrodecusto.nome_centro, centrodecusto.centro_de_custo, centrodecusto.user_respon])

        return response

class ExportarCentrodeCustoExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='urf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Numero Centro de Custo', 'Nome Centro de Custo', 'Centro de Custo', 'Usuário Responsável']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        dados = CentroDeCusto.objects.all()

        row_num = 1

        for centrodecusto in dados:
            ws.write(row_num, 0, centrodecusto.id, font_style)
            ws.write(row_num, 1, centrodecusto.numero_centro, font_style)
            ws.write(row_num, 2, centrodecusto.nome_centro, font_style)
            ws.write(row_num, 3, centrodecusto.centro_de_custo, font_style)
            #ws.write(row_num, 4, centrodecusto.user.username, font_style)


            row_num += 1

        wb.save(response)
        return response
