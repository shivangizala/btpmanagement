from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("myprojects", views.myprojects, name="myprojects"),
    path("profile", views.profile, name="profile"),
    path("timetable", views.timetable, name="timetable"),

]

