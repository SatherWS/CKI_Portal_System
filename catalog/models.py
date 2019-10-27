from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save

# Club Chapters Available 
class Club_Chapter (models.Model):
    club_id = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=30)
    state = models.CharField(max_length=4)
    total_members = models.IntegerField(null = True, default = 0)
    service_hours = models.IntegerField(null = True, default = 0)
    donations_raised = models.IntegerField(null = True, default = 0)

    def __str__(self):
        return self.school_name

# Custom UserManager model that gets rid of usernames and declares unique emails"""
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True

    def _create_user(self, email, password, club_id, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.set_club_id(club_id)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

# User Model """
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD  = 'email'
    chapter = models.ForeignKey('Club_Chapter',on_delete=models.PROTECT)
    ranking = models.CharField(default='member', max_length=20)
    total_service_hours = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_dollars_raised = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    REQUIRED_FIELDS = []
    objects = UserManager()

"""
#@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=40, default=None)
    ranking = models.CharField(default='member', max_length=20)
"""

# All columns of service_project table
class Service_Project(models.Model):
    project_ID = models.IntegerField(primary_key=True)
    club_chapter = models.ForeignKey('Club_Chapter',on_delete=models.PROTECT)
    project_title = models.CharField(max_length=15, help_text='Enter field documentation')
    project_duration = models.CharField(max_length=15, help_text='Enter field documentation')
    project_location = models.CharField(max_length=15, help_text='Enter field documentation')
    project_leader = models.CharField(max_length=15, help_text='Enter field documentation')
    project_date = models.CharField(max_length=15, help_text='Enter field documentation')
    members_needed = models.IntegerField(default=4)
    wait_list = models.IntegerField(default=2)
    
    
    # Metadata: ordering of records and such
    class Meta: 
        db_table = 'catalog_service_project'

    # String representation of weekly_projects model 
    def __str__(self):
        return self.project_title

# Associative Entity for auth_user and service_project relationship """
# IN PROGRESS 
class work_order(models.Model):
    work_order_id = models.IntegerField(primary_key=True)
