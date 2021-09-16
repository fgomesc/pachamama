from django.urls import path
from . views import home, register, budget, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('register-base/', register, name='register_base'),
    path('budget/', budget, name='budget'),
    path('dashboard/', dashboard, name='dashboard'),
]
