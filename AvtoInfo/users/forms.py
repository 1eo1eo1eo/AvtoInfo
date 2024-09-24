from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    email = forms.CharField()


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

    email = forms.CharField()
