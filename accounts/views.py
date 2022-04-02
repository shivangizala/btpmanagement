from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def createProject(request):
    if request.method == 'POST':
        title = request.POST['title']
        username = request.POST['username']
        # user1=User(username=username)
        # slug = request.POST['slug']
        publish_date = request.POST['publish_date']
        content = request.POST['content']
        status = request.POST['status']
        total_applications = int(request.POST['total_applications'])
        user1=User.objects.filter(username=username)

        for u in user1:
            author_id=u.id
        project = BtpProject.objects.create(title=title, author_id=author_id, publish_date=publish_date, content=content, status=status, total_applications=total_applications )
        project.save()
        # print('user created')
        return redirect('homepage')
    else:
        return render(request,'createProject.html')  

@login_required(login_url='/')
def homepage(request):
    if request.method == 'POST':
        search_value = request.POST['search_value']
        #serach value is username/author
        user1=User.objects.filter(username=search_value)
        for u in user1:
            author_id=u.id     
        all_projects=BtpProject.objects.filter(author_id=author_id, status='open')
        context={
            'projects':all_projects
        }
        return render(request,'homepage.html', context)
    else:
        all_projects=BtpProject.objects.filter(status='open')
        context={
            'projects':all_projects
        }
        return render(request,'homepage.html', context) 

@login_required(login_url='/')
def myprojects(request):
    username=request.user.username    
    users=User.objects.filter(username=username)
    for u in users:
            author_id=u.id
    all_projects=BtpProject.objects.filter(author_id=author_id)
    context={
        "all_projects":all_projects
    }

    return render(request,'myprojects.html',context)  

@login_required(login_url='/')
def profile(request):
    return render(request,'profile.html')  

@login_required(login_url='/')
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