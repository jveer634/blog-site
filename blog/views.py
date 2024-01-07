from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from  .models import Blog
from .forms import BlogForm


class BlogList(generic.ListView):
    model = Blog
    template_name="blog_list.html"


class BlogDetail(generic.DetailView):
    model = Blog
    template_name="blog_detail.html"

    

class BlogCreate(LoginRequiredMixin, generic.CreateView):
    model = Blog
    form_class = BlogForm
    template_name="blog_create.html"

class BlogUpdate(LoginRequiredMixin, generic.UpdateView):
    model= Blog
    form_class = BlogForm
    template_name="blog_update.html"

class BlogDelete(LoginRequiredMixin, generic.DeleteView):
    model=Blog
    success_url ="/blog"
    template_name="blog_delete.html"