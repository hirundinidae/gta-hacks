from rest_framework import serializers
from .models import Profile, Resource
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "bio", "school", "province")

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ("name", "questions", "answers")


