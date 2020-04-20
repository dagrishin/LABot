from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('user', 'word_translation', 'word_to_learn')


admin.site.register(Word, WordAdmin)
