from django.db import models
from registration.models import User


class Word(models.Model):
    user = models.ForeignKey(
        User,
        related_name="users_word",
        on_delete=models.CASCADE,
    )
    word_translation = models.CharField(max_length=150)
    word_to_learn = models.CharField(max_length=150)
    description = models.TextField()
    word_image = models.ImageField(upload_to="Word_Images", blank=True)
    word_status = models.IntegerField(default=1)
