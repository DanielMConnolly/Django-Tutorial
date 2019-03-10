from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=50)

    @classmethod
    def create(cls, title, body, author):
        post = cls(title=title, body=body, author=author)
