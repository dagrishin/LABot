from rest_framework import serializers

from registration.models import User
from tickets.models import Word


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class WordSerializers(serializers.ModelSerializer):
    """Сериализация карточки"""
    user = UserSerializer()

    class Meta:
        model = Word
        fields = ("id", "user", "word_translation", "word_to_learn", "description")


# class WordPostSerializers(serializers.ModelSerializer):
#     """Сериализация карточки"""
#
#     class Meta:
#         model = Word
#         fields = ("user", "word_translation", "word_to_learn", "description")

