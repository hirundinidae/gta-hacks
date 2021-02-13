from django.shortcuts import render
from .models import Profile, Resource
from .serializers import ProfileSerializer, ResourceSerializer
from rest_framework import viewsets
from django.http import JsonResponse
# from rest_framework import generics
# from django.views.generic import TemplateView

# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    viewset = viewsets.ModelViewSet
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get(self, viewset):
        return JsonResponse(queryset)


class ResourceView(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
