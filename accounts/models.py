from django.db import models

# Create your models here.
class Student(models.Model):
    cpi=models.IntegerField(default=0)