from rest_framework import serializers

from registration.models import User
from tickets.models import Word


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class WordSerializer(serializers.ModelSerializer):
    """Сериализация карточки"""
    user = UserSerializer()

    class Meta:
        model = Word
        fields = ("id", "user", "word_translation", "word_to_learn", "description")


class WordDetailSerializer(serializers.ModelSerializer):
    """Сериализация карточки"""
    user = UserSerializer()

    class Meta:
        model = Word
        fields = ("id", "user", "word_translation", "word_to_learn", "description")


class WordCreateSerializer(serializers.ModelSerializer):
    """Сериализация карточки"""

    class Meta:
        model = Word
        fields = ("word_translation", "word_to_learn", "description")

    def create(self, validated_data):
        word = Word.objects.update_or_create(**validated_data)
        return word



