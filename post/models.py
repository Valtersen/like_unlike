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

    def liked(self, user_id):
        liked = True if Like.objects.filter(user=user_id, post=self.id).exists() else False
        return liked


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_user')

    def __str__(self):
            return f'post:{self.post.heading}, user: {self.user.id}'
