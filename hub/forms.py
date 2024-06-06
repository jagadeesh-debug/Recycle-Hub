from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Custom_User


class Signup(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ["username", "email", "password", "mobile"]
