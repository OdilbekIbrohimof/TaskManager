from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SimpleUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'birthday', 'direction', 'phone_number', "password1", "password2"]
        

class ProfileEditForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'img', 'birthday', 'phone_number', 'telegram_link', 'instagram_link', 'facebook_link']