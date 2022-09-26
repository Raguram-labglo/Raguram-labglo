from django.shortcuts import render
from django.views import generic
from .models import *


class Add_employee(generic.CreateView):

    model = Employee
    fields = '__all__'
    template_name = 'add_emp.html'
    success_url = 'http://127.0.0.1:8000/'
    
 
class Add_department(generic.CreateView):
    
    model = Department
    fields = '__all__'
    template_name = 'add_emp.html'
    success_url = 'http://127.0.0.1:8000/'


