from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics

# Create your views here.

class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
