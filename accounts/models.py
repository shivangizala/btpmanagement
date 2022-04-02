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

class BtpProject(models.Model):
    options={
        ('open','Open'),
        ('closed','Closed')
    }
    title = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=100, null=True, blank=True)
    publish_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    content=models.TextField(default="", blank=True)
    status = models.CharField(max_length=100, choices=options, default='open')
    total_applications=models.IntegerField(default=0)
    def __str__(self):
       return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=BtpProject)  
