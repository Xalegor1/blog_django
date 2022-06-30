from urllib.error import HTTPError
from django.shortcuts import render
from django.http import *
from .models import Post, User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.



# def index(request):
#     context = {
#         'posts' : Post.objects.all(),
#         'users' : User.objects.all()
#     }   
#     return render(request, "core/index.html", context)



def about(request):
    return render(request, "core/about.html", {'title': 'About page!'})    



class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
        


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post        



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']    
    template_name = 'core/post_create.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']    
    template_name = 'core/post_update.html'

    def form_valid(self, form):        
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'core/post_delete.html'
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  