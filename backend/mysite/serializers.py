from rest_framework import serializers
from .models import Profile, Resource, tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "bio", "school", "province")

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = ("__all__")

class ResourceSerializer(serializers.ModelSerializer):
    tag_list = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Resource
        fields = ("name", "questions", "answers", "tag_list")



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
