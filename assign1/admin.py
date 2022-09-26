from django.contrib import admin
from assign1.models import *

class Stu_view(admin.ModelAdmin):

    list_display = ('id','roll_no','name','profile')
    
    
admin.site.register(Student, Stu_view)


class Mark_view(admin.ModelAdmin):

    list_display = ('id','student_num','M1','M2','M3','M4','M5')
admin.site.register(Mark, Mark_view)
# Register your models here.
