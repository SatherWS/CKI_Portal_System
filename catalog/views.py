from django.shortcuts import render,redirect
from catalog.models import Service_Project,User,Club_Chapter,ProjectRegistration, Donation_Drive,Donation
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from datetime import datetime, timedelta
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from catalog.forms import SignUpForm
from django.views.generic.edit import FormView

# Home Page View
def index(request):
    return render(request, 'index.html')

# User dashboard view
def dashboard(request):
    return render(request, 'catalog/dashboard.html')

# Used for dashboard -- d/n work 11/15/2019
def UserTotals(request):
    totals = User.objects.filter(
        ProjectRegistration__user = 'request.user'
    ).annotate(
        total_hrs = Sum('projectregistration__service_hrs')
    )
    context = {'totals': totals}
    return render(request, 'catalog/base_generic.html', context)

# Club Chapter totals | members, service hours and dollars raised for charities
def ClubTotals(request):
    clubs = Club_Chapter.objects.annotate(
        total_users=Count('user'),
        total_hrs=Sum('projectregistration__service_hrs')
    ).order_by('-club_id')
    
    context = {'clubs': clubs}
    return render(request, 'catalog/club_chapter_list.html', context)

# temporary use to restric access for non logged in users
@login_required
def members_only(request):
   return render(request, 'catalog/user_auth_test.html')

# Service Projects (Starts Here)
class ProjectsListView(generic.ListView):
   template_name = 'catalog/service_project_list.html'
   context_object_name = 'service_project_list'

   def get_queryset(self):
       return Service_Project.objects.all()

# Service Project related views
class ExtraContextMixin(object):
    def extra(self):
        return dict()

class DetailView(ExtraContextMixin, generic.DetailView):
    model = Service_Project
    template_name = 'catalog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExtraContextMixin, self).get_context_data(**kwargs)
        context['extra'] = ProjectRegistration.objects.all()
        return context
    
# project_add_worker & project_remove_worker functions here
def project_add_worker(request, project_id):
    if request.method == 'POST':
        this_project = Service_Project.objects.get(pk=project_id)
        # Find time delta
        delta = this_project.datetime_end - this_project.datetime_start
        if delta.days < 0:
            delta = timedelta(days=0,
            seconds=delta.seconds, microseconds=delta.microseconds)
        # Divide difference in seconds by number of seconds in hour (3600)  
        delta_hours = delta.total_seconds() / 3600
        this_project.add_user_to_list_of_workers(
            user=request.user, 
            chapter=request.user.chapter, 
            hrs=delta_hours
        )
        return redirect('catalog:detail', pk=project_id)

def project_remove_worker(request, project_id):
    if request.method == 'POST':
        this_project = Service_Project.objects.get(pk=project_id)
        this_project.remove_user_from_list_of_workers(user=request.user)
        return redirect('catalog:service_project')
# Service Projects End

# Donation Drives Starts 
"""
class DrivesListView(generic.ListView):
    template_name = 'catalog/donation_drive_list.html'
    context_object_name = 'donation_drive_list'

    def get_queryset(self):
        return Donation_Drive.objects.all()

class DriveDetailView(generic.DetailView):
    model = Donation_Drive
    template_name = 'catalog/drive_detail.html'
"""
# Donation Drive Section Ends Here

# Signup Form View
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            university = form.cleaned_data.get('university')
            user = form.save()
            login(request, user)
            return redirect('catalog:index')
    else:
        form = SignUpForm()
    return render(request, 'catalog/signup.html', {'form': form})
