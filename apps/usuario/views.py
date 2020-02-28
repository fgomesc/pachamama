import xlwt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Usuario
from django.views import View
import csv




class UsuarioList(LoginRequiredMixin, ListView):
    model = Usuario

class UsuarioEdit(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['primeiro_nome', 'ultimo_nome', 'email', 'centrodecusto_usuario', 'perfil_usuario', 'permissao_usuario']

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('list_usuario')

class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['primeiro_nome', 'ultimo_nome', 'email', 'centrodecusto_usuario', 'perfil_usuario','permissao_usuario']


    def form_valid(self, form):
        usuario = form.save(commit=False)
        username = usuario.primeiro_nome.lower() + usuario.ultimo_nome.lower()
        usuario.user = User.objects.create(username=username)
        usuario.save()
        return super(UsuarioCreate, self).form_valid(form)

class ExportarUsuarioCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        dados = Usuario.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Primeiro Nome', 'Ultimo Nome', 'Email', 'Usuário', 'Perfil', 'Permissão'])
        for usuario in dados:
            writer.writerow([usuario.id, usuario.primeiro_nome, usuario.ultimo_nome, usuario.email, usuario.user, usuario.perfil_usuario, usuario.permissao_usuario])

        return response

class ExportarUsuarioExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='urf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Primeiro Nome', 'Ultimo Nome', 'email', 'Usuário', 'Centro de Custo', 'Perfil', 'Permissao']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        dados = Usuario.objects.all()

        row_num = 1

        for usuario in dados:
            ws.write(row_num, 0, usuario.id, font_style)
            ws.write(row_num, 1, usuario.primeiro_nome, font_style)
            ws.write(row_num, 2, usuario.ultimo_nome, font_style)
            ws.write(row_num, 3, usuario.email, font_style)
            ws.write(row_num, 4, usuario.user.username, font_style)
            #ws.write(row_num, 5, usuario.centrodecusto_usuario, font_style)
            #ws.write(row_num, 6, usuario.perfil_usuario, font_style)
            #ws.write(row_num, 7, usuario.permissao_usuario, font_style)


            row_num += 1

        wb.save(response)
        return response