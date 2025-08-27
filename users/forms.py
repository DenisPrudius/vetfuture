from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomAuthenticationForm(AuthenticationForm):
    model = User
    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )



class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Підтвердити пароль",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Логін",
            "email": "Email",
        }

        def clean_email(self):
            email = self.cleaned_data["email"]
            if User.objects.filter(email=email).exists():
                raise ValidationError("Цей email вже використовується.")
            return email

        def clean_username(self):
            username = self.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                raise ValidationError("Цей username вже зайнятий.")
            return username

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        labels = {
            "first_name": "Ім'я",
            "last_name": "Прізвище",
            "email": "Email",
        }