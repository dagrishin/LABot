from django import forms
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm

from .models import User
from user_option.models import TimeInterval, Status


class UserRegisterForm(UserCreationForm, PasswordResetForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self, commit=True, **kwargs):
        user = self.instance
        if not user.id:
            # user.is_active = False # Активация через почту
            user.is_active = True # Активация через телграм
            user = super(UserRegisterForm, self).save()
            PasswordResetForm.save(self, **kwargs)
        return user


class UserActivationRegisterForm(forms.Form):
    class Meta:
        model = User

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.user.is_active = True
        if commit:

            self.user.save()
        return self.user


class UserActivationForm(forms.Form):

    reg_key = forms.CharField()
