from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    vote_count = models.IntegerField(default=1)
    author = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "stories"
        ordering = ['-published_date']

    def __str__(self):
        return self.title
