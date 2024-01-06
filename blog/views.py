from django.shortcuts import render

from django.views import generic

from  .models import Blog

# Create your views here.


class BlogList(generic.ListView):
    model = Blog
    template_name="blog_list.html"
    # queryset = Blog.objects.all()


class BlogDetail(generic.DetailView):
    model = Blog
    template_name="blog_detail.html"
    # queryset = Blog.objects.all()
