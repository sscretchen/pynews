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


class Vote(models.Model):
    story = models.ForeignKey(Story, related_name='votes', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.story.vote_count = self.story.vote_count + 1
        self.story.save()

        super(Vote, self).save(*args, **kwargs)


class Comment(models.Model):
    story = models.ForeignKey(Story, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=255)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plural = 'comments'
        ordering = ['-published_date']

    def __str__(self):
        return self.author
