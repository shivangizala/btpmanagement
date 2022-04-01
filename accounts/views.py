from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# Create your views here.


def index(request):
    return render(request, "index.html")

#def register(request):
    return render(request, "register.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
# Create your views here. 

def project(request, slug_text):
    q=BtpProject.objects.filter(slug=slug_text)
    all_projects=BtpProject.objects.all()
    if q.exists():
        q=q.first()
    else:
        return HttpResponse("<h1>page not found</h1>")
    context={
        'post':q,
        'projects':all_projects

    }
    return render(request,'project.html', context)  

def createProject(request):
    if request.method == 'POST':
        print('ssssssssssssssssssssssssssssssssssssssssssssssssss')
        title = request.POST['title']
        project = BtpProject(title=title)
        project.save()
        print('user created')
        return redirect('homepage')
    else:
        return render(request,'createProject.html')  

def homepage(request):
    all_projects=BtpProject.objects.filter(status='open')
    context={
        'projects':all_projects
    }
    return render(request,'homepage.html', context) 

def myprojects(request):
    return render(request,'myprojects.html')  

def profile(request):
    return render(request,'profile.html')  

def timetable(request):
    return render(request,'timetable.html')  


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("homepage")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html')  

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        is_student=request.POST['is_student']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')      