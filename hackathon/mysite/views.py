from django.shortcuts import render

def profile_view(request):
  
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
