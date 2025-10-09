from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):
    '''
    Post Model Schema
    '''
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
 

    def __str__(self) -> str:
        return self.title
