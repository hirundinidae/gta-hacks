from django.shortcuts import render, redirect
from .models import Profile
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import createProfile, createUser
from django.contrib.auth.models import User

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

@login_required (redirect_field_name='/')
def profile_view(request):
    profs = Profile.objects.get(user = request.user)
    print(profs)
    context = {
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

