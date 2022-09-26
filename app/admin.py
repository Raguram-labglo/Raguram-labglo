from django.contrib import admin
from app.models import GeeksModel
class sub(admin.ModelAdmin):
    list_display = ('id','title','description','last_modified','img')
admin.site.register(GeeksModel,sub)
# Register your models here.

