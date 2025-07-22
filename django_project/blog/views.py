from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all(),

    }
    return render(request, 'blog/blog_index.html', context)

def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'blog/about_us.html', context)