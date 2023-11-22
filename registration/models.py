from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    reg_ok = models.BooleanField(
        default=False,
    )
    reg_key = models.CharField(
        _("Registration key"),
        max_length=10,
        default=123,
    )
    chat_id = models.IntegerField(
        _("Telegram User ID"),
        blank=True,
        null=True,
    )
