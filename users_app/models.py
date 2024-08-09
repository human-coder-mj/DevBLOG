from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    img = models.ImageField(default="default.jpg" , upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self):
        super().save()


        upload_img = Image.open(self.img.path)

        if upload_img.height > 300 or upload_img.width > 300:
            output_size = (300 , 300)
            upload_img.thumbnail(output_size)
            upload_img.save(self.img.path)