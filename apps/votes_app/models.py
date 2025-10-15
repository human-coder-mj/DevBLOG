from django.db import models
from django.contrib.auth.models import User
from user_posts.models import UserPost

class Votes(models.Model):
    VOTE_CHOICES = [
        ("UPVOTE", "upvote"),
        ("DOWNVOTE", "downvote"),
    ]
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.CharField(choices=VOTE_CHOICES, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vote
