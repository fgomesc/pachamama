from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

posts = [
    {
        'author': 'Felipe Gomes',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'Felipe Costa',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 27, 2018'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'core/home.html', context)

@login_required
def register(request):
    return render(request, 'core/register_base.html', {'title': 'Register'})

@login_required
def budget(request):
    return render(request, 'core/budget.html', {'title': 'Budget'})

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', {'title': 'Dashboard'})