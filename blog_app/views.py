from django.shortcuts import render
from .models import Posts
# from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Blog-Home</h1>")



#Home page view
def home(request):
    context = {
        "posts" : Posts.objects.all()
    }
    return render(request , "blog_html_templates/home.html" ,context)





def about(request):
    return render(request , "blog_html_templates/about.html" , {"title" : "About"})