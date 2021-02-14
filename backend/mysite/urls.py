from rest_framework import routers
from django.urls import path, include
from . import views
# from django.contrib.auth.urls import 

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'profiles/?', views.ProfileView, 'profiles')
router.register(r'resources/?', views.ResourceView, 'resources')
router.register(r'pin/?', views.PinView, 'pin')

urlpatterns = [
#     path('api/', views.ProfileListCreate.as_view()),
    path('api/', include(router.urls)),
    path('account/register', views.UserCreate.as_view(), ),
    path('profile/register', views.ProfileCreate.as_view(), name='create'),
    path('', include("django.contrib.auth.urls")),
]
