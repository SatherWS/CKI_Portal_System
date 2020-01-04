from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime 

# Club Chapters Available """
class Club_Chapter(models.Model):
    club_id = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=30)
    state = models.CharField(max_length=4)

    def __str__(self):
        return self.school_name
    
# Custom UserManager model that replaces usernames for unique emails"""
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
    # nothing happens when deleting _ character before ('email address') -- migrations may be fucked
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD  = 'email'
    chapter = models.ForeignKey('Club_Chapter',on_delete=models.PROTECT)
    ranking = models.CharField(default='member', max_length=20)
    
    # may not use total hours and dollars fields
    total_service_hours = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    total_dollars_raised = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        ordering = ('email',)

    def __str__(self):
        return self.email

# Projects Availabe for Certain Clubs """
class Service_Project(models.Model):
    project_ID = models.IntegerField(primary_key=True)
    club_chapter = models.ForeignKey('Club_Chapter',on_delete=models.PROTECT)
    project_title = models.CharField(max_length=15, help_text='Enter field documentation')
    project_location = models.CharField(max_length=15, help_text='Enter field documentation')
    project_leader = models.CharField(max_length=15, help_text='Enter field documentation')
    datetime_start = models.DateTimeField(help_text='Enter field documentation')
    datetime_end = models.DateTimeField(help_text='Enter field documentation')
    members_needed = models.IntegerField()
    wait_list = models.IntegerField()
    
    class Meta:
        ordering = ('project_title',)
        db_table = 'catalog_service_project'

    def add_user_to_list_of_workers(self, user, chapter, hrs):
        now = datetime.datetime.now()
        registration = ProjectRegistration.objects.create(
                                                        user = user,
                                                        chapter = chapter,
                                                        project = self,
                                                        time_registered = now,
                                                        service_hrs = hrs)

    def remove_user_from_list_of_workers(self, user):
        registration = ProjectRegistration.objects.get(user = user, project = self)
        registration.delete()

    # String representation of service_project model 
    def __str__(self):
        return self.project_title

    def get_registrations(self):
        return ProjectRegistration.objects.filter(project = self)

# Associative Model where project sign up data is stored
class ProjectRegistration(models.Model):
    project = models.ForeignKey(Service_Project, verbose_name='Project',on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='Worker',on_delete=models.CASCADE)
    chapter = models.ForeignKey(Club_Chapter, verbose_name='Club', on_delete=models.CASCADE)
    time_registered = models.DateTimeField()
    service_hrs = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Worker for project'
        verbose_name_plural = 'Workers for projects'
        ordering = ['time_registered',]
        unique_together = ('user','project')
    
    def save(self, *args, **kwargs):
        if self.id is None and self.time_registered is None:
            self.time_registered = datetime.datetime.now()
        super(ProjectRegistration, self).save(*args, **kwargs)

# Donation_Drive entity followed by corresponding associative entity
class Donation_Drive(models.Model):
    chapter = models.ForeignKey(Club_Chapter, verbose_name='Club', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, help_text='Enter field documentation')
    goal = models.DecimalField(max_digits=20, decimal_places=2)
    datetime_start = models.DateTimeField(help_text='Enter field documentation')
    datetime_end = models.DateTimeField(help_text='Enter field documentation')

class Donation(models.Model):
    drive = models.ForeignKey(Donation_Drive, verbose_name='Drive',on_delete=models.PROTECT)
    chapter = models.ForeignKey(Club_Chapter, verbose_name='Donation', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='Worker',on_delete=models.CASCADE)
    time_donated = models.DateTimeField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)

