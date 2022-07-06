from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

class PostList(ListView):
    queryset= Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(DetailView):
    model = Post
    template_name= 'post_detail.html'

class AddPost(CreateView):
    model = Post
    template_name= 'addPost.html'
    fields = '__all__'