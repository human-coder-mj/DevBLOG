from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''
    User Profile Schema
    '''
    ROLE_CHOICES = [
        ("ADMIN", "admin"),
        ("MEMBER", "member")
    ]
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    username= models.CharField(max_length=20)
    role = models.CharField(choices=ROLE_CHOICES, default="MEMBER")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} Profile"