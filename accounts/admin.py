from django.contrib import admin
from .models import *
# Register your models here.
class BtpProjectAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','status')
    
class CollegePeopleAdmin(admin.ModelAdmin):
    list_display=('name','course','cpi','is_student')

class NotificationAdmin(admin.ModelAdmin):
    list_display=('name','moment','content')

class ProjectMemberAdmin(admin.ModelAdmin):
    list_display=('name','accept_status')

class MomAdmin(admin.ModelAdmin):
    list_display=('project','description')

class TeamNotificationAdmin(admin.ModelAdmin):
    list_display=('project','agenda')

class EventAdmin(admin.ModelAdmin):
    list_display=('date','agenda')

admin.site.register(BtpProject, BtpProjectAdmin)
admin.site.register(CollegePeople, CollegePeopleAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(ProjectMember, ProjectMemberAdmin)
admin.site.register(Mom, MomAdmin)
admin.site.register(TeamNotification, TeamNotificationAdmin)
admin.site.register(Event, EventAdmin)


