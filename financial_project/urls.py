from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from apps.users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('usuario/', include('apps.usuario.urls')),
    path('cliente/', include('apps.cliente.urls')),
    path('centrodecusto/', include('apps.centro_de_custo.urls')),
    path('naturezaorcamentaria/', include('apps.natureza_orcamentaria.urls')),
    path('perfil/', include('apps.perfil.urls')),
    path('permissao/', include('apps.permissao.urls')),
    path('cadastro-orcamento/', include('apps.cadastro_orcamento.urls')),
    path('cadastro-estouro-orcamento/', include('apps.estouro_orcamento.urls')),
    path('movimento-dia/', include('apps.mov_dia.urls')),
    path('', include('apps.core.urls')),
]
