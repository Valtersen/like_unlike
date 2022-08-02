from django.contrib.auth.models import User
from django.db import models



class Post(models.Model):
    heading = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):      # If python2 use __str__ if python3
            return self.heading

    @property
    def total_likes(self):
        return self.likes.count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_user')


