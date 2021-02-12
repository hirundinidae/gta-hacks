from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.ProfileListCreate.as_view()),
]
