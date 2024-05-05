from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.post.title} - {self.caption}"


