from django.db import models
from registration.models import User


def time_gen():
    t = []
    for i in range(25):
        t.append((f"{i}", f"{i}:00"))
    return t


class TimeInterval(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_intervals",
        on_delete=models.CASCADE,
    )
    TIME_INTERVAL = time_gen()
    time_start = models.CharField(
        max_length=2, choices=TIME_INTERVAL, default=TIME_INTERVAL[12][0]
    )
    time_end = models.CharField(
        max_length=2, choices=TIME_INTERVAL, default=TIME_INTERVAL[18][0]
    )


class RepeatAmount(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_repeats",
        on_delete=models.CASCADE,
    )
    words_per_day = models.IntegerField(
        default=10,
    )


class Status(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_word_status",
        on_delete=models.CASCADE,
    )
    #
    status1 = models.IntegerField(default=300)
    #
    status2 = models.IntegerField(default=900)
    #
    status3 = models.IntegerField(default=2700)
    #
    status4 = models.IntegerField(default=7200)
    #
    status5 = models.IntegerField(default=18000)
    #
    status6 = models.IntegerField(default=86400)
    #
    status7 = models.IntegerField(default=259200)
    #
    status8 = models.IntegerField(default=2592000)
