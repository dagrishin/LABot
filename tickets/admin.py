from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Word


class WordAdminForm(forms.ModelForm):
    description = forms.CharField(label=_("Описание"), widget=CKEditorUploadingWidget())

    class Meta:
        model = Word
        fields = '__all__'


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """Фильмы"""
    # list_display = '__all__'

    form = WordAdminForm