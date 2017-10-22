from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """blog标题"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title
