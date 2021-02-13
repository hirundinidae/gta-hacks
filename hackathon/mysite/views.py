from django.shortcuts import render, redirect
from .models import Profile, Pin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import createProfile, createUser, submitResource
from django.contrib.auth.models import User
from haystack.generic_views import SearchView, SearchQuerySet
from haystack.forms import ModelSearchForm
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

@login_required 
def profile_view(request):
    profs = Profile.objects.get(user = request.user)
    print(profs)
    pins = Pin.objects.all()
    userPins = pins.filter(prof = profs)
    Rform = submitResource()
    if request.method=='POST':
        print("POSTTTTT")
        Rform = submitResource(request.POST, request.FILES, )
        if Rform.is_valid():
            print("VALIDDD")
            Rform.clean()
            Rform.save()
        
    context = {
        'Rform': Rform,
        'pins': userPins,
        'profile': profs
    }
    return render(request, 'home.html', context)




def create_view(request):
    Uform = createUser()
    Pform = createProfile()
    context = {
        'Uform': Uform,
        'Pform': Pform
    }
    if request.method == 'POST':
        print('FORM-POSTTTTTT')
        Uform = createUser(request.POST)
        Pform = createProfile(request.POST)
        if Uform.is_valid() and Pform.is_valid():
            print('VALID')
            name = Uform.cleaned_data.get('username')
            print(name)
            Uform.save()
            obj = User.objects.get(username=name)
            print(obj.id)
            p = Profile(user=obj, bio=Pform.cleaned_data.get('bio'), school=Pform.cleaned_data.get('school'), province=Pform.cleaned_data.get('province'))
            p.save()
            return redirect('/login')

    return render(request, 'create.html', context)
class Searcher(SearchView):
    queryset=SearchQuerySet().order_by('score')
    form_class=ModelSearchForm

