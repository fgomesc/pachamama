import csv

import xlwt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Permissao
from django.views import View


class PermissaoList(LoginRequiredMixin, ListView):
    model = Permissao

class PermissaoEdit(LoginRequiredMixin, UpdateView):
    model = Permissao
    fields = ['tipo_permissao']

class PermissaoDelete(LoginRequiredMixin, DeleteView):
    model = Permissao
    success_url = reverse_lazy('list_permissao')


class PermissaoCreate(LoginRequiredMixin, CreateView):
    model = Permissao
    fields = ['tipo_permissao']


class ExportarPermissaoCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        dados = Permissao.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Tipo de Permissão'])
        for permissao in dados:
            writer.writerow([permissao.id, permissao.tipo_permissao])

        return response

class ExportarPermissaoExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='urf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Tipo de Permissão']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        dados = Permissao.objects.all()

        row_num = 1

        for permissao in dados:
            ws.write(row_num, 0, permissao.id, font_style)
            ws.write(row_num, 1, permissao.tipo_permissao, font_style)


            row_num += 1

        wb.save(response)
        return response
