from django.shortcuts import render

from django.views import generic

from  .models import Blog
from .forms import BlogForm

# Create your views here.


class BlogList(generic.ListView):
    model = Blog
    template_name="blog_list.html"
    # queryset = Blog.objects.all()


class BlogDetail(generic.DetailView):
    model = Blog
    template_name="blog_detail.html"
    # queryset = Blog.objects.all()


class BlogCreate(generic.CreateView):
    model = Blog
    form_class = BlogForm
    template_name="blog_create.html"


