from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=100) # title will a field in our post table in the database
    #title will be a character field with a max_length = 100 

    content = models.TextField()
    # textfield is multiple lines of text 

    date_posted = models.DateTimeField(default=timezone.now)
    # auto_now parameter set as True is updates the date and time of post ,every time the post was updated
    # auto_now_add parameter set as True , it will set the date_posted to current date-time only when the post is created , but this will never update the date posted 

    author = models.ForeignKey(User , on_delete=models.CASCADE)
    # on_delete parameter does that on deltetion of user after creating a post , then the post should also get deleted

    def __str__(self) -> str:
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse('post-detail' , kwargs={'pk': self.pk})