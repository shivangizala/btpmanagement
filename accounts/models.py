from sys import maxsize
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import *

from accounts.utils import unique_slug_generator

# Create your models here.    

class CollegePeople(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    course = models.CharField(max_length=100, default="")
    cpi=models.DecimalField(default=0, max_digits=3, decimal_places=1)
    is_student=models.BooleanField(default=True)

class Notification(models.Model):
    name= models.ForeignKey(User, on_delete=models.CASCADE, default="")
    moment = models.DateTimeField(default=timezone.now)
    content=models.CharField(max_length=100, default="")

class BtpProject(models.Model):
    options={
        ('open','Open'),
        ('closed','Closed')
    }
    title = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=100, null=True, blank=True)
    # , input_formats=['%Y-%m-%d', ] do this formatting in forms
    publish_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    content=models.TextField(default="", blank=True)
    status = models.CharField(max_length=100, choices=options, default='open') #accepted,requested, decline all
    total_applications=models.IntegerField(default=0)
    students_required=models.IntegerField(default=0)
    projectid=models.CharField(max_length=10, default="")
    grade=models.IntegerField(default=0)
    def __str__(self):
       return self.title

class ProjectMember(models.Model):
    options={
        ('accepted','accepted'),
        ('rejected','rejected'),
        ('requested','requested')#when applied but not accepted or rejected yet. unconfirmed.
    }
    project=models.ManyToManyField(BtpProject)
    name=models.ForeignKey(User, on_delete=models.CASCADE, default="")
    accept_status=models.CharField(max_length=100, choices=options, default='rejected')
    options2={
        ('taken','taken'),
        ('not taken','not taken'),
    }
    student_status=models.CharField(max_length=100, choices=options2, default='not taken')

class Mom(models.Model):
    date = models.DateField(default=timezone.now)
    agenda=models.TextField(default="", blank=True)
    description=models.TextField(default="", blank=True)
    project=models.ForeignKey(BtpProject, on_delete=models.CASCADE, default="")
    minutes=models.IntegerField(default=0)
    points=models.IntegerField(default=0)

class TeamNotification(models.Model): #like meeting create delete any news
    date = models.DateTimeField(default=timezone.now)
    project=models.ForeignKey(BtpProject, on_delete=models.CASCADE, default="")
    agenda=models.TextField(default="", blank=True)

class Event(models.Model):
    date = models.DateField(default=timezone.now)
    agenda=models.TextField(default="", blank=True)
    name=models.ForeignKey(User, on_delete=models.CASCADE, default="")

# class Meeting:
#     date = models.DateField(default=timezone.now)
#     agenda=models.TextField(default="", blank=True)
#     project=models.ForeignKey(BtpProject, on_delete=models.CASCADE, default="")


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=BtpProject)  
