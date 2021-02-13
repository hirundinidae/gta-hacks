from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets
# from rest_framework import generics
# from django.views.generic import TemplateView

# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
