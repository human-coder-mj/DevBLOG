from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts
from django.views.generic import (
    ListView , DetailView , CreateView , UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

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

#About Page View
def about(request):
    return render(request , "blog_html_templates/about.html" , {"title" : "About"})