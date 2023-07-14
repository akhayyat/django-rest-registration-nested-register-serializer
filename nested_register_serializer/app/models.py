from django.contrib.auth.models import AbstractUser
from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)


class User(AbstractUser):
    primary_channel = models.OneToOneField(
        Channel,
        on_delete=models.PROTECT,
        related_name="owner",
    )
