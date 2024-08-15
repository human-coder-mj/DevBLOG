from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from .models import Posts
from django.views.generic import (
    ListView , DetailView , CreateView , UpdateView , DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User

# def home(request):
#     return HttpResponse("<h1>Blog-Home</h1>")



#Home page view
# def home(request):
#     context = {
#         "posts" : Posts.objects.all()
#     }
#     return render(request , "blog_html_templates/home.html" ,context)

class PostListView(ListView):
    model = Posts
    template_name = "blog_html_templates/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"] #for ordering the blogs according to the date posted , with the newest blog at top
    paginate_by = 4
    pass

#Post Detail Page View
class PostDetailView(DetailView):
    model = Posts
    template_name = "blog_html_templates/post_detail.html"
    pass

class PostCreateView(LoginRequiredMixin , CreateView):
    model = Posts
    fields = ['title' , 'content']
    template_name = "blog_html_templates/post_form.html"
    success_url = '/'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    pass

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin ,  UpdateView):
    model = Posts
    fields = ['title' , 'content']
    template_name = "blog_html_templates/post_form.html"
    success_url = "/"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Posts
    template_name = "blog_html_templates/post_confirm_delete.html"
    success_url = "/"


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    pass

class UserPostListView(ListView):
    model = Posts
    template_name = "blog_html_templates/user_post.html"
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Posts.objects.filter(author = user).order_by('-date_posted')

    pass

#About Page View
def about(request):
    return render(request , "blog_html_templates/about.html" , {"title" : "About"})