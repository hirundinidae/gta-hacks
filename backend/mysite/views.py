from django.shortcuts import render, redirect
from .models import Profile, Resource
from .serializers import ProfileSerializer, ResourceSerializer, UserSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import filters
# from rest_framework import generics
# from django.views.generic import TemplateView

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
class ProfileView(viewsets.ModelViewSet):
    viewset = viewsets.ModelViewSet
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get(self, viewset):
        return JsonResponse(queryset)


class ResourceView(viewsets.ModelViewSet):
    search_fields = ['name', 'tag_list__name']
    filter_backends = (filters.SearchFilter,)
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    viewset = viewsets.ModelViewSet
    serializer_class = UserSerializer
    # permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        response = super(UserCreate, self).create(request, *args, **kwargs)
        # here may be placed additional operations for
        # extracting id of the object and using reverse()
        return redirect('create')

    # permission_classes = (AllowAny, )


class ProfileCreate(generics.CreateAPIView):
    viewset = viewsets.ModelViewSet
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
