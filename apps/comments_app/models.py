from django.db import models
from user_posts.models import UserPost
from django.contrib.auth.models import User

class Comment(models.Model):
    '''
    Comment Model Schema
    '''
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content