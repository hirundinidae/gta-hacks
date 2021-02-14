from django.shortcuts import render, redirect
from .models import Profile, Resource, Pin, MyUser
from .serializers import ProfileSerializer, ResourceSerializer, UserSerializer, RegisterSerializer, PinSerializer, MyUserSerializer, RegisterUserSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import filters
# from rest_framework import generics
# from django.views.generic import TemplateView

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User, AbstractBaseUser

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

class PinView(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer

class UserCreate(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegisterUserSerializer
    def create(self, request, *args, **kwargs):
        response = super(UserCreate, self).create(request, *args, **kwargs,)
        return redirect('/api-auth/login')

    # permission_classes = (AllowAny, )


class ProfileCreate(generics.CreateAPIView):
    viewset = viewsets.ModelViewSet
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # def create(self, request, *args, **kwargs):
    #     response = super(ProfileCreate, self).create(request, *args, **kwargs,)


class MyUserView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def retrieve(self, request, pk=None):
        queryset = MyUser.objects.all()
        user = get_object_or_404(queryset, username=pk)
        serializer = MyUserSerializer(user)
        return Response(serializer.data)





from django.contrib.auth.forms import AuthenticationForm

def Login(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            print('REDIRECT')
            return redirect('/api/users/username')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return redirect('/api-auth/login')