from django.db import models
# from registration.models import User

from tickets.models import Word


class Main(models.Model):
    word = models.ForeignKey(
        Word,
        related_name='words',
        on_delete=models.CASCADE,
    )
    send_time = models.DateTimeField()
    if_send = models.BooleanField(
        default=False,
    )

