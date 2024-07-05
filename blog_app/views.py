from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Blog-Home</h1>")


blog_posts = [
    {
        "author" : "Manas Jha",
        "title" : "Blog Post 1",
        "content" : "First post content",
        "date_posted" : "July 25 2024",
    },
    {
        "author" : "Paras",
        "title" : "Blog Post 2",
        "content" : "second post content",
        "date_posted" : "July 26 2024",
    },
    {
        "author" : "Kartik Gupta",
        "title" : "Blog Post 3",
        "content" : "Third post content",
        "date_posted" : "July 27 2024",
    }   
]


#Home page view
def home(request):
    context = {
        "posts" : blog_posts
    }
    return render(request , "html_templates/home.html" ,context)





def about(request):
    return render(request , "html_templates/about.html" , {"title" : "About"})