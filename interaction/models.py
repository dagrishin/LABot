from django.db import models
# from registration.models import User
<<<<<<< HEAD
from tickets.models import Word
=======
from ticket.models import Word
>>>>>>> a50e5e180b94a9057b343b48d032034622a0c316

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

