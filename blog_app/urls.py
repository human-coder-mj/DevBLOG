from django.urls import path
from . import views
# from django.http import HttpResponse
 
urlpatterns = [
    # path('', lambda resp:HttpResponse("<h1> Empty-Route </h1>")
    #       , name="empty-route"),

    path('' , views.home , name="blog-home"), #for enabling this as the default page now the first page open will be the home page
# here the name parameter is the URL pattern name  for the 
    path("about/" , views.about , name="blog-about")
]