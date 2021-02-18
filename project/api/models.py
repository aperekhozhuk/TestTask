from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login = models.DateField(null=True)
    last_request = models.DateField(null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Post(models.Model):
    # Warning: changing 'max_length' value demands Database migration
    title = models.CharField(blank=False, max_length=300)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)


class Like(models.Model):
    class Meta:
        unique_together = [
            ["post", "user"],
        ]

    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
