from django.shortcuts import render
from .models import Profile, Resource
from .serializers import ProfileSerializer, ResourceSerializer
from rest_framework import viewsets
# from rest_framework import generics
# from django.views.generic import TemplateView

# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ResourceListView(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
