from django.contrib import admin
from app2.models import *
from django.contrib.admin.views.main import ChangeList
from app2.forms import MovieChangeListForm


#class display_Employee(admin.ModelAdmin):
#    list_display = ("name", "department", "age")
#    list_filter = ('name', 'age')
#    search_fields = ('department')
    #self.list_editable         
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Posting)
