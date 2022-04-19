from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("create-project", views.createProject, name="create-project"),
    path("homepage", views.homepage, name="homepage"),
    path("myprojects/<int:profile_id>", views.myprojects, name="myprojects"),
    path("profile/<int:profile_id>", views.profile, name="profile"),
    path("profile/<int:profile_id>/edit", views.profileEdit, name="profile-edit"),
    path("timetable", views.timetable, name="timetable"),
    path("notification", views.notification, name="notification"),
    path("project/<slug:slug_text>", views.project, name="project"),
    path("project/<slug:slug_text>/edit", views.projectEdit, name="project-edit"),
    path("project/<slug:slug_text>/delete", views.projectDelete, name="project-delete"),
    path("project/<slug:slug_text>/mom", views.projectMom, name="project-mom"),
    path("project/<slug:slug_text>/notification/create", views.projectNotificationCreate, name="project-notification-create"),    
    path("project/<slug:slug_text>/mom/create", views.projectMomCreate, name="project-mom-create"),
    path("project/<slug:slug_text>/mom/edit/<int:mom_id>", views.projectMomEdit, name="project-mom-edit"),
    path("project/<slug:slug_text>/mom/delete/<int:mom_id>", views.projectMomDelete, name="project-mom-delete"),
    path("project/<slug:slug_text>/requests", views.projectRequests, name="project-requests"),
    path("project/<slug:slug_text>/requests/accept/<int:profile_id>", views.projectRequestsAccept, name="project-accept"),
    path("project/<slug:slug_text>/requests/decline/<int:profile_id>", views.projectRequestsDecline, name="project-decline"),
]

