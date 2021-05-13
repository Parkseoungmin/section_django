from django.shortcuts import render
from .models import Blog

# Create your views here.

def main(request):
    return render(request, 'main.html')

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})