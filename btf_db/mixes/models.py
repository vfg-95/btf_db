from django.db import models


class Mix(models.Model):

    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(
        upload_to='images/', blank=False
    )
    content = models.TextField(blank=False)
    audio = models.URLField(blank=True)
    draft = models.BooleanField()
    posted_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return f'{self.id} {self.title}'
