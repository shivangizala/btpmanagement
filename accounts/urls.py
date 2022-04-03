from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("create-project", views.createProject, name="create-project"),
    path("homepage", views.homepage, name="homepage"),
    path("myprojects", views.myprojects, name="myprojects"),
    path("profile", views.profile, name="profile"),
    path("profile/<slug:username_text>/edit", views.profileEdit, name="profile-edit"),
    # path("profile/<slug:username_text>/delete", views.profileDelete, name="profile-delete"),
    path("timetable", views.timetable, name="timetable"),
    path("project/<slug:slug_text>", views.project, name="project"),
    path("project/<slug:slug_text>/edit", views.projectEdit, name="project-edit"),
    path("project/<slug:slug_text>/delete", views.projectDelete, name="project-delete"),


]

