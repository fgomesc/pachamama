from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from financial_project.users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('usuario/', include('financial_project.usuario.urls')),
    path('cliente/', include('financial_project.cliente.urls')),
    path('centrodecusto/', include('financial_project.centro_de_custo.urls')),
    path('naturezaorcamentaria/', include('financial_project.natureza_orcamentaria.urls')),
    path('perfil/', include('financial_project.perfil.urls')),
    path('permissao/', include('financial_project.permissao.urls')),
    path('cadastro-orcamento/', include('financial_project.cadastro_orcamento.urls')),
    path('cadastro-estouro-orcamento/', include('financial_project.estouro_orcamento.urls')),
    path('movimento-dia/', include('financial_project.mov_dia.urls')),
    path('contas-a-pagar/', include('financial_project.contas_a_pagar.urls')),
    path('produto/', include('financial_project.produto.urls')),
    path('estoque/', include('financial_project.estoque.urls')),
    path('', include('financial_project.core.urls')),

]
