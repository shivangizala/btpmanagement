from django.contrib import admin
from .models import *
# Register your models here.
class BtpProjectAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','status')

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(BtpProject, BtpProjectAdmin)


