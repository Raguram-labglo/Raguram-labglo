from django.urls import path
from .views import *

urlpatterns = [path('add_emp', Add_employee.as_view(), name = 'add_emp'),
               path('add_dept',Add_department.as_view(),name = 'add_dept')]

