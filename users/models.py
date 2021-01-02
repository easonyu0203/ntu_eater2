from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pictures/default.jpg',
                              upload_to='profile_pictures')

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        MAX_SIZE = (400, 400)
        img.thumbnail(MAX_SIZE)
        img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} profile'
