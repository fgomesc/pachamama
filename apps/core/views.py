from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'core/home.html')

@login_required
def register(request):
    return render(request, 'core/register_base.html', {'title': 'Register'})

@login_required
def budget(request):
    return render(request, 'core/budget.html', {'title': 'Budget'})

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', {'title': 'Dashboard'})