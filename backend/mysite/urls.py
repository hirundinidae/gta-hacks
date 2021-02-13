from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'profiles/?', views.ProfileView, 'profiles')
router.register(r'resources/?', views.ResourceView, 'resources')

urlpatterns = [
#     path('api/', views.ProfileListCreate.as_view()),
    path('api/', include(router.urls)),
    path('account/register', views.UserCreate.as_view())
]
