from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(
        upload_to='images/', blank=False
    )
    content = models.TextField(blank=False)
    audio_one = models.URLField(blank=True)
    audio_two = models.URLField(blank=True)
    audio_three = models.URLField(blank=True)
    audio_four = models.URLField(blank=True)
    audio_five = models.URLField(blank=True)
    draft = models.BooleanField()
    posted_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return f'{self.id} {self.title}'
