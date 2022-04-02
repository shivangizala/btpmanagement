from django.contrib import admin
from .models import *
# Register your models here.
class BtpProjectAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','status')
    
class CollegePeopleAdmin(admin.ModelAdmin):
    list_display=('name','course','cpi','is_student')

admin.site.register(BtpProject, BtpProjectAdmin)
admin.site.register(CollegePeople, CollegePeopleAdmin)
