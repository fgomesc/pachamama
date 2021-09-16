import csv

import xlwt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Perfil
from django.views import View


class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil


class PerfilEdit(LoginRequiredMixin, UpdateView):
    model = Perfil
    fields = ['tipo_perfil']


class PerfilDelete(LoginRequiredMixin, DeleteView):
    model = Perfil
    success_url = reverse_lazy('list_perfil')


class PerfilCreate(LoginRequiredMixin, CreateView):
    model = Perfil
    fields = ['tipo_perfil']

class ExportarPerfilCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        dados = Perfil.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Tipo de Perfil'])
        for perfil in dados:
            writer.writerow([perfil.id, perfil.tipo_perfil])

        return response

class ExportarPerfilExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='urf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Tipo de Perfil']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        dados = Perfil.objects.all()

        row_num = 1

        for perfil in dados:
            ws.write(row_num, 0, perfil.id, font_style)
            ws.write(row_num, 1, perfil.tipo_perfil, font_style)

            row_num += 1

        wb.save(response)
        return response