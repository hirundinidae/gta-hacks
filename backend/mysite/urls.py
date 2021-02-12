from django.urls import path
from . import views

urlpatterns = [
    path('api/mysite/', views.ProfileListCreate.as_view()),
]
