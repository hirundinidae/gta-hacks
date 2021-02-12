from django.urls import path
from . import views
from .views import HomePageView, profile_view, create_view

app_name = 'mysite'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', profile_view, name='profile'),
    path('create/', create_view, name='create'),
]

