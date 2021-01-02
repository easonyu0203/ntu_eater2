from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from restaurants.models import Restaurant


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        upload_to='blog_pictures', default='blog_pictures/default.jpg'
    )
    comment_on = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='comments')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
