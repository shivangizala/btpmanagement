from django.db import models

# Create your models here.
class Student(models.Model):
    userName = models.CharField(max_length=100, default="")
    firstNAme = models.CharField(max_length=100, default="")
    lastName = models.CharField(max_length=100, default="")
    course = models.CharField(max_length=100, default="")
    cpi=models.IntegerField(default=0)

class Professor(models.Model):
    userName = models.CharField(max_length=100, default="")
    firstNAme = models.CharField(max_length=100, default="")
    lastName = models.CharField(max_length=100, default="")

class Project(models.Model):
    ProjectId = models.CharField(max_length=100, default="")
    firstNAme = models.CharField(max_length=100, default="")
    lastName = models.CharField(max_length=100, default="")