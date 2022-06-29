from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, User
# Create your views here.



def index(request):
    context = {
        'posts' : Post.objects.all(),
        'users' : User.objects.all()
    }   
    return render(request, "core/index.html", context)



def about(request):
    return render(request, "core/about.html", {'title': 'About page!'})    