from datetime import timedelta, datetime
from django.utils.translation import gettext_lazy as _
import pytz
from django.db import models

from tickets.models import Word


class WordData(models.Model):
    class Meta:
        index_together = [
            ["if_send", "send_time", "active"],
        ]
        ordering = ['-start', 'data_add', 'send_time']
    word = models.ForeignKey(
        Word,
        related_name='worddata',
        on_delete=models.CASCADE,
    )
    send_time = models.DateTimeField(default=datetime.now(tz=pytz.utc), db_index=True)
    if_send = models.BooleanField(default=False, db_index=True)
    start = models.IntegerField(default=0)
    active = models.BooleanField(default=True, db_index=True)
    data_add = models.DateTimeField(default=datetime.now(tz=pytz.utc))


    def __str__(self):
        return self.word.word_translation

    def save(self, *args, **kwargs):
        if not self.pk:
            if WordData.objects.filter(word__user_id=self.word.user_id, if_send=True)\
                    and not WordData.objects.filter(word__user_id=self.word.user_id, if_send=False):
                self.if_send = True

        super(WordData, self).save(*args, **kwargs)



class WordSend(models.Model):
    word = models.ForeignKey(
        Word,
        related_name='wordsend',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.word.word_translation

