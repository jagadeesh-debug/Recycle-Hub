from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Custom_User,Map


class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
class Mapform(forms.ModelForm):
    class Meta:
        model=Map
        fields=["place"]
