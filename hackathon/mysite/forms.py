from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Resource

class createProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      'school',
      'province',
      'bio'
    ]

class createUser(UserCreationForm):
  class Meta:
    model = User
    fields = [
      'username',
      'email',
      'password1',
      'password2'
    ]

class submitResource(forms.ModelForm):
  class Meta:
    model = Resource
    fields = [
      'name',
      'questions',
      'answers',
    ]


