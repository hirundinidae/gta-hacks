from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.SimpleRouter()
router.register(r'profiles', views.ProfileView, 'profiles')

urlpatterns = [
#     path('api/', views.ProfileListCreate.as_view()),
    path('api/', include(router.urls))
]
