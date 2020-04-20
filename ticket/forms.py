from django import forms


class WordCreateForm(forms.Form):
    word_translation = forms.CharField()
    word_to_learn = forms.CharField()
    word_image = forms.ImageField()


class ValidPk(forms.Form):
    pk = forms.ModelChoiceField(queryset=None, required=True)


class ValidSlug(forms.Form):
    slug = forms.ModelChoiceField(queryset=None, required=True)
