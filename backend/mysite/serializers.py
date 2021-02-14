from rest_framework import serializers
from .models import Profile, Resource, tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import HttpRequest
from django.http import HttpResponse
# from flask import request

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("bio", "school", "province")
    def create(self, validated_data):
        print(self.request.user)
        obj = User.objects.get(username='PersonA')
        # p = Profile(user=obj, bio=Pform.cleaned_data.get('bio'), school=Pform.cleaned_data.get('school')province=Pform.cleaned_data.get('province'))
        # p.save()
        print(obj)
        prof = Profile(
            user=obj,
            bio=validated_data['bio'],
            school=validated_data['school'],
            province=validated_data['province']
        )
        print('MADE')
        prof.save()
        return prof

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

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
