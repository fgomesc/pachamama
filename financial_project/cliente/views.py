import csv

import xlwt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from django.views import View

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteEdit(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nome_cliente', 'centro_de_custo_cliente', 'user_cliente']

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_cliente')

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nome_cliente', 'centro_de_custo_cliente', 'user_cliente']

class ExportarClienteCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        dados = Cliente.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id','Nome Cliente', 'Centro de Custo Cliente', 'Responsável Cliente'])
        for cliente in dados:
            writer.writerow([cliente.id, cliente.nome_cliente, cliente.centro_de_custo_cliente, cliente.user_cliente])

        return response

class ExportarClienteExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='urf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id','Nome Cliente', 'Centro de Custo Cliente', 'Responsável Cliente']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        dados = Cliente.objects.all()

        row_num = 1

        for cliente in dados:
            ws.write(row_num, 0, cliente.id, font_style)
            ws.write(row_num, 1, cliente.nome_cliente, font_style)
            #ws.write(row_num, 2, cliente.centro_de_custo_cliente, font_style)
            #ws.write(row_num, 3, cliente.user_cliente, font_style)


            row_num += 1

        wb.save(response)
        return response
