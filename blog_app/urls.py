from django.urls import path
from . import views
from .views import PostListView , PostDetailView ,PostCreateView
# from django.http import HttpResponse
 
urlpatterns = [
    # path('', lambda resp:HttpResponse("<h1> Empty-Route </h1>")
    #       , name="empty-route"),

    path('' , PostListView.as_view() , name="blog-home"), #for enabling this as the default page now the first page open will be the home page
    #here the name parameter is the URL pattern name  for the 
    path('post/<int:pk>/' , PostDetailView.as_view() , name="post-detail"),
    path('post/new/' , PostCreateView.as_view() , name="post-create"),
    path("about/" , views.about , name="blog-about")
]