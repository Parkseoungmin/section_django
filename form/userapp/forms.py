from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import utils

from django.contrib.auth.forms import UserCreationForm

from .models import Blog, CustomUser

class BlogForm(forms.ModelForm):
    class Meta():
        model = Blog
        fields = ['title', 'writer', 'body','image']

class RegistorForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1','password2', 'nick_name','university', 'location']