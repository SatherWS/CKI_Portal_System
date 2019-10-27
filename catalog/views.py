from django.shortcuts import render,redirect
from catalog.models import Service_Project,User,Club_Chapter
from django.views import generic
from django.contrib.auth.decorators import login_required

# Home Page ----------------------------------------------
def index(request):
    return render(request, 'index.html')

# Club Searcher ------------------------------------------
def FindClub(request):
    return render(request, 'catalog/club_search.html')

# Service Projects ---------------------------------------
#@login_required --- Needs show club specific projects
class ProjectsListView(generic.ListView):
   model = Service_Project

@login_required
def members_only(request):
   return render(request, 'catalog/user_auth_test.html')


# Sign Form Code -----------------------------------------
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from catalog.forms import SignUpForm

# Sign Up Form -------------------------------------------
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            university = form.cleaned_data.get('university')
            if Club_Chapter.objects.get(school_name = university):
                user = form.save()
                login(request, user)
                return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'catalog/signup.html', {'form': form})
"""
# Part 2 Sign Up Form ------------------------------------
def signup2(request):
    if request.method == 'POST':
        form = SignUpFormPart2(request.POST)
        if form.is_valid():
            form.save()
            user.refresh_from_db()
            user.profile.university = form.cleaned_data.get('university')
            user.profile.club_id = form.cleaned_data.get('club_id')
            login(request, user)
            return redirect('index')
    else:
        form = SignUpFormPart2()
    return render(request, 'catalog/signup2.html', {'form': form})
"""