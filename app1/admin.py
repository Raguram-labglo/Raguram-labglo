from django.contrib import admin
from .models import detiles_form
class li(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','age')
admin.site.register(detiles_form,li)

# Register your models here.
