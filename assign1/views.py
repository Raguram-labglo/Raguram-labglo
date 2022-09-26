from django.shortcuts import render,redirect
from .form import *
from assign1.models import *
from django.http import HttpResponse

def add_form(request):

    form = Student_form(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        
    return render(request, 'add_student.html', {'data':form})
    
    
def add_marks(request):

    form1 = Mark_form(request.POST or None, request.FILES or None)
    
    if form1.is_valid():
        form1.save()
        
    return render(request, 'add_marks.html', {'mark':form1})  
    
    
def show(request):

    stud = Student.objects.all()
    marks1 = Mark.objects.all()
    context = {'stu':stud,'mar':marks1}
    return render(request, 'show_details.html', context)  
    
    
def show_mark(request,id):

    mar = Mark.objects.filter(student_num_id = id).values()
    return render(request, 'show_mark.html',{'mar':mar})
    return redirect('show')
    
    
def update_stu(request,id):

    mar = Student.objects.get(id = id)
    form2 = Student_form(request.POST or None, request.FILES or None, instance = mar) 
    if form2.is_valid():
        form2.save()  
    return render(request, 'update_stu.html',{'form':form2})
    
    
def update_mark(request,id):

    mar1 = Mark.objects.get(id = id)
    mark1 = Mark_form(request.POST or None, request.FILES or None, instance = mar1) 
    print(mark1)
    if mark1.is_valid():
        mark1.save()  
    return render(request, 'update_mark.html',{'mark1':mark1})
    return redirect('/show/')  # 4

    
    
def del_student(request,id):

    stu = Student.objects.get(id = id)
    stu.delete()
    return HttpResponse("deleted")
    
def del_mark(request,id):

    mark_del = Mark.objects.get(id = id)
    mark_del.delete()
    return HttpResponse("mark deleted")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
