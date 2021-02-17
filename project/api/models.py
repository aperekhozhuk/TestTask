from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # Warning: changing 'max_length' value demands Database migration
    title = models.CharField(blank=False, max_length=300)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
