from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    intro = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
