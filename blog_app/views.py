from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView , DetailView
# from django.http import HttpResponse

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

#About Page View
def about(request):
    return render(request , "blog_html_templates/about.html" , {"title" : "About"})