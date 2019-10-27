from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('clubs/', views.FindClub, name='clubs'),
    path('ServiceProjects/', views.ProjectsListView.as_view(), name='service_project'),
    path('members/', views.members_only, name='members-only'),
    path('signup/', views.signup, name='signup')
    #path('signup2/', views.signup2, name='signup-part-2')
]