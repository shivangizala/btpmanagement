from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from django.shortcuts import get_object_or_404
# from django.core.mail import send_mail
# print("11111111111111111111")
# print(u)
# print("111111111111111111")

# @login_required(login_url='/')
# def projectApply(request, slug_text):
#     if request.method == 'POST':
#         return redirect( 'project/slug_text')
#     else:
        # return render(request,'project.html', context)  

@login_required(login_url='/')
def projectNotificationCreate(request, slug_text):
    u=get_object_or_404(User, username=request.user.username)  
    q=get_object_or_404(CollegePeople, name_id=u.id)
    agenda = request.POST['agenda']
    notify = TeamNotification.objects.create(agenda=agenda, project_id=q.id )
    notify.save()
    if request.method == 'POST':
        team_member=ProjectMember.objects.filter(project__id=q.id, accept_atatus='accepted')
        for tm in team_member:
            

        url="/project/"+slug_text+ "/notification"
        return redirect(url)
    else:
        if u.id==q.author_id:    
            same_user=True
        else:
            same_user=False
        context={
            'alug':q.slug,
            'same_user':same_user
        }
        return render(request,'projectNotificationCreate.html', context) 

@login_required(login_url='/')
def projectMom(request, slug_text):
    if request.method == 'POST':
        pass        
    else:
        #check if requesting person is in team
        u=get_object_or_404(User, username=request.user.username)
        c=get_object_or_404(CollegePeople, name_id=u.id)
        q=get_object_or_404(BtpProject, slug=slug_text)
        team_prof=False
        in_team= False
        if c.is_student==False: 
            if c.name_id==u.id: #prof who created
                team_prof=True
            else:
                team_prof=False
        else:
            pm = ProjectMember.objects.filter(name_id=u.id, project__id=q.id, accept_status="accepted")
            if pm.exists():
                pm=pm.first()
                in_team=True
            else:
                in_team=False
                return HttpResponse("<h1>page not found</h1>")
        all_mom = Mom.objects.filter( project__id=q.id)
        context={
            'team_prof':team_prof,
            'in_team':in_team,
            'all_mom':all_mom,
            'title':q.title,
            'slug':q.slug
        }
        return render(request,'projectMom.html', context)  

@login_required(login_url='/')
def projectMomEdit(request, slug_text, mom_id):
    if request.method == 'POST':
        q=get_object_or_404(Mom, id=mom_id) 
        agenda = request.POST['agenda']
        date = request.POST['date']
        points = request.POST['points']
        description = request.POST['description']
        minutes = request.POST['minutes']
        Mom.objects.filter(id=mom_id).update(agenda=agenda, date=date, points=int(points), description=description, minutes=int(minutes))
        url="/project/"+slug_text+ "/mom"
        return redirect(url)
    else:
        q=get_object_or_404(Mom, id=mom_id) 
        context={
            'slug_text':slug_text,
            'q':q
        }
        u=get_object_or_404(User, username=request.user.username)  
        if u.id==q.author_id:    
            return render(request,'projectMomEdit.html', context) 
        else:
            return HttpResponse("<h1>page not found</h1>")

@login_required(login_url='/')
def projectMomCreate(request, slug_text):
    if request.method == 'POST':
        agenda = request.POST['agenda']
        date = request.POST['date']
        points = request.POST['points']
        description = request.POST['description']
        minutes = request.POST['minutes']
        q=get_object_or_404(BtpProject, slug=slug_text) 
        mom = Mom.objects.create(agenda=agenda, date=date, points=int(points), description=description, minutes=int(minutes), project_id=q.id )
        mom.save()
        url="/project/"+slug_text+ "/mom"
        return redirect(url)
    else:

        context={
            'slug_text':slug_text,
        }
        u=get_object_or_404(User, username=request.user.username)  
        if u.id==q.author_id:    
            return render(request,'projectMomCreate.html', context) 
        else:
            return HttpResponse("<h1>page not found</h1>")

@login_required(login_url='/')
def projectMomDelete(request, slug_text, mom_id):
    if request.method == 'POST':
        pass
    else:
        u=get_object_or_404(User, username=request.user.username)  
        a=get_object_or_404(BtpProject, slug=slug_text) 
        if u.id==a.author_id:    
            q=get_object_or_404(Mom, id=mom_id) 
            q.delete()
            url="/project/"+slug_text+ "/mom"
            return redirect(url) 
        else:
            return HttpResponse("<h1>page not found</h1>")
        
@login_required(login_url='/')
def projectRequestsAccept(request, slug_text, profile_id):
    q=get_object_or_404(BtpProject, slug=slug_text)
    if request.method == 'POST':
        value = request.POST['value']
        if value=='accept':
            pm = ProjectMember.objects.filter( project__id=q.id,name_id=profile_id)
            pm=pm.first()
            pm.accept_status='accepted'
            pm.save()
            u=get_object_or_404(User, username=request.user.username)
            content= "you are accepted in "+ q.title
            n = Notification.objects.create(name_id=profile_id, content=content)
            n.save()
        # else: #value=decline
        #     pm = ProjectMember.objects.filter( project__id=q.id,name_id=profile_id)
        #     pm=pm.first()
        #     pm.delete()
        url='/project/'+slug_text+'/requests' #vvvvvvvvvvvvimp
        return redirect( url)
    else:
        return HttpResponse("<h1>page not found</h1>")

@login_required(login_url='/')
def projectRequestsDecline(request, slug_text, profile_id):
    q=get_object_or_404(BtpProject, slug=slug_text)
    if request.method == 'POST':
        value = request.POST['value']
        if value=='decline':
            pm = ProjectMember.objects.filter( project__id=q.id,name_id=profile_id)
            pm=pm.first()
            pm.delete()
            u=get_object_or_404(User, username=request.user.username)
            content= "you are rejected in "+ q.title
            n = Notification.objects.create(name_id=profile_id, content=content)
            n.save()
        url='/project/'+slug_text+'/requests' #vvvvvvvvvvvvimp
        return redirect(url)
    else:
        return HttpResponse("<h1>page not found</h1>")

@login_required(login_url='/')
def projectRequests(request, slug_text):
    if request.method == 'POST':
        pass
    else:
        u=get_object_or_404(User, username=request.user.username)
        q=get_object_or_404(BtpProject, slug=slug_text)
        pm = ProjectMember.objects.filter( project__id=q.id, accept_status='requested')
        all_requests=pm
        context={
            'all_requests':all_requests,
            'title':q.title,
            'slug':slug_text,
        }
        #check if its the same user
        if u.id==q.author_id:    
            return render(request,'projectRequests.html', context)  
        else:
            return HttpResponse("<h1>page not found</h1>")
        
@login_required(login_url='/')
def profile(request, profile_id):
    if request.method == 'POST':
        pass
    else:
        u=get_object_or_404(User, id=profile_id)
        u2=get_object_or_404(User, username=request.user.username)
        q=get_object_or_404(CollegePeople, name_id=u.id)
        if u2.id==profile_id:
            same_user=True
        else:
            same_user=False
        context={
            'u':u, #user object
            'q':q, #cp object
            'same_user':same_user
        }
        return render(request,'profile.html', context)

@login_required(login_url='/')
def profileEdit(request, profile_id):
    if request.method == 'POST':
        u=get_object_or_404(User, username=request.user.username)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        cpi = request.POST['cpi']
        course = request.POST['course']
        User.objects.filter(id=u.id).update(first_name=first_name, last_name=last_name)
        CollegePeople.objects.filter(name_id=profile_id).update(cpi=cpi, course=course)
        return redirect( 'profile')
    else:
        u=get_object_or_404(User, username=request.user.username)
        q=get_object_or_404(CollegePeople, name_id=u.id)
        context={
            'u':u, #user object
            'q':q #cp object
        }
        if u.id==profile_id:
            return render(request,'profileEdit.html', context)
        else:
            return HttpResponse("<h1>page not found</h1>")

@login_required(login_url='/')
def project(request, slug_text):
    #0-rejected 1-accepted 2-requested
    if request.method == 'POST':
        u=get_object_or_404(User, username=request.user.username)
        q=get_object_or_404(BtpProject, slug=slug_text)
        status_value=request.POST['accept_status']
        if status_value=='apply':#means that user is either rejected or requested status
            set_status='requested'
            pm = ProjectMember.objects.create(name_id=u.id, accept_status=set_status)
            pm.save()
            pm.project.add(q)
            pm.save()
            content=u.first_name+" "+ u.last_name + " has applied for "+ q.title
            n = Notification.objects.create(name_id=q.author_id, content=content)
            n.save()
        else: # status_value=='withdraw':
            set_status='rejected'
            pm = ProjectMember.objects.filter(name_id=u.id, project__id=q.id)
            pm=pm.first()
            pm.delete()
            content=u.first_name+" "+ u.last_name + " has withdrawn from "+ q.title
            n = Notification.objects.create(name_id=q.author_id, content=content)
            n.save()
        url='/myprojects/' + str(u.id)
        return redirect(url)
    else:
        u=get_object_or_404(User, username=request.user.username)
        c=get_object_or_404(CollegePeople, name_id=u.id)
        q=get_object_or_404(BtpProject, slug=slug_text)
        team = ProjectMember.objects.filter( project__id=q.id, accept_status='accepted')
        #check if its the same user
        if u.id==q.author_id:    
            same_user=True
        else:
            same_user=False
        is_student=c.is_student
        pm = ProjectMember.objects.filter(name_id=u.id, project__id=q.id)
        
        if pm.exists():
            pm=pm.first()
            set_status=pm.accept_status
            if set_status=='accepted':
                set_status=1
            elif set_status=='rejected':
                set_status=0
            else :
                set_status=2
        else:
            set_status=0#'rejected'

        #check if student is in team
        pm = ProjectMember.objects.filter(name_id=u.id, project__id=q.id, accept_status="accepted")
        if pm.exists():
            pm=pm.first()
            in_team=True
        else:
            in_team=False

        context={
            'setted_status':set_status,
            'post':q,
            'is_student':is_student,
            'same_user':same_user,
            'team':team,
            'in_team':in_team
        }
        return render(request,'project.html', context)  

@login_required(login_url='/')
def projectDelete(request, slug_text):
    if request.method == 'POST':
        pass
    else:
        q=get_object_or_404(BtpProject, slug=slug_text)
        u=User.objects.get(username=request.user.username)
        #see if its the creator of the project or not
        if u.id==q.author_id:
            q.delete()
        return redirect(request, 'homepage')

@login_required(login_url='/')
def projectEdit(request, slug_text):
    if request.method == 'POST':
        publish_date = request.POST['publish_date']
        content = request.POST['content']
        status = request.POST['status']
        grade = request.POST['grade']
        grade=int(grade)
        BtpProject.objects.filter(slug=slug_text).update(publish_date=publish_date, content=content, status=status , grade=grade)
        return redirect( 'myprojects')
    else:
        #find project using slug in request
        q=get_object_or_404(BtpProject, slug=slug_text)
        u=get_object_or_404(User, username=request.user.username)  
        context={
            'post':q
        }
        if u.id==q.author_id:    
            return render(request,'projectEdit.html', context)
        else:
            return HttpResponse("<h1>page not found</h1>")

@login_required(login_url='/')
def createProject(request):
    if request.method == 'POST':
        title = request.POST['title']
        publish_date = request.POST['publish_date']
        content = request.POST['content']
        status = request.POST['status']
        u=get_object_or_404(User, username=request.user.username)  
        project = BtpProject.objects.create(title=title, author_id=u.id, publish_date=publish_date, content=content, status=status )
        project.save()
        return redirect('homepage')
    else:
        #whole below process to check if the user is is_Student or not
        u=get_object_or_404(User, username=request.user.username)  
        q=get_object_or_404(CollegePeople, name_id=u.id)
        if q.is_student==False:
            return render(request,'createProject.html')
        else:
            return HttpResponse("<h1>page not found</h1>")

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
        #whole below process to check if the user is is_Student or not
        u=get_object_or_404(User, username=request.user.username)
        q=get_object_or_404(CollegePeople, name_id=u.id)
        all_projects=BtpProject.objects.filter(status='open')
        is_student=q.is_student
        context={
            'projects':all_projects,
            'is_student': is_student,
            'id':u.id,          
        }
        return render(request,'homepage.html', context) 

@login_required(login_url='/')
def myprojects(request, profile_id): #id of person who created it
    u=get_object_or_404(User, username=request.user.username)#person who is trying to access
    c=get_object_or_404(CollegePeople, name_id=u.id)
    is_student=c.is_student
    if c.is_student==False:
        all_projects=BtpProject.objects.filter(author_id=u.id)
    else:
        all_projects = ProjectMember.objects.filter( name_id=u.id)
    if u.id==profile_id:    
        same_user=True
    else:
        same_user=False
    context={
        "all_projects":all_projects,
        'is_student':is_student,
        'same_user': same_user
    }
    return render(request,'myprojects.html',context)  

@login_required(login_url='/')
def timetable(request):
    return render(request,'timetable.html')  

@login_required(login_url='/')
def notification(request):
    u=get_object_or_404(User, username=request.user.username)
    q=Notification.objects.filter(name_id=u.id).order_by('-moment')
    context={
        'q':q
    }
    return render(request,'notification.html',context)  
    
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
        #     send_mail(
        #         'hello there, login is successful',
        #         'this is automated',
        #         'shivuhaters@gmail.com',
        #         [user.email],
        #         fail_silently=False
        #     )
            u=get_object_or_404(User, username=request.user.username)  
            n = Notification.objects.create(name_id=u.id, content="Login attempted")
            n.save()
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
                user.save()
                if is_student=='student':
                    is_student=True
                else:
                    is_student=False

                collegePerson=CollegePeople.objects.create(name_id=user.id, is_student=is_student)
                collegePerson.save()
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

def index(request):
    return render(request, "index.html")