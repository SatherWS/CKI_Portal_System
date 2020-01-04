from django.urls import path
from . import views
from django.urls import include, path
from django.conf.urls import url

# Now this shits the bed
app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('data/', views.UserTotals, name='data'),
    path('clubs/', views.ClubTotals, name='clubs'),
    #path('charities/', views.DrivesListView.as_view(), name='donation_drives'),
    #path('<int:pk>/', views.DriveDetailView.as_view(), name='donation'), 
    path('ServiceProjects/', views.ProjectsListView.as_view(), name='service_project'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), 
    path('<int:project_id>/project_add_worker', views.project_add_worker, name='project_add_worker'),
    path('<int:project_id>/project_remove_worker', views.project_remove_worker, name='project_remove_worker'),
    path('members/', views.members_only, name='members-only'),
    path('signup/', views.signup, name='signup'),
    
]