from django.contrib import admin
from catalog.models import Service_Project, User, Club_Chapter
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

# Register User Models
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','chapter')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','email','chapter', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'chapter','first_name', 'last_name', 'is_staff', 
    'ranking','total_service_hours','total_dollars_raised')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

# Register Club Chapters
class AvailableClubs(admin.ModelAdmin):
    list_display = ('club_id', 'school_name', 'state')
    
admin.site.register(Club_Chapter, AvailableClubs)

# Register Service Projects.
class projectsAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'club_chapter','project_leader', 'project_duration','project_date',
    'project_location','project_ID')

admin.site.register(Service_Project, projectsAdmin)
