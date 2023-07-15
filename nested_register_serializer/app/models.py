from collections import OrderedDict
from typing import Any
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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if isinstance(kwargs.get("primary_channel", None), OrderedDict):
            kwargs["primary_channel"] = Channel(**kwargs["primary_channel"])
        super().__init__(*args, **kwargs)
