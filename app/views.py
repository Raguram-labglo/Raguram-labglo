from django.shortcuts import render
from .form import GeeksForm
from .models import GeeksModel
def home_view(request):
    context ={}
  
    form = GeeksForm(request.POST,request.FILES)
     
    if form.is_valid():
        form.save()
   
    context['val'] = form
    return render(request, "home.html", context)
    
    
def read_view(request):
    
    read_obj = GeeksModel.objects.all().values()
    return render(request, "update.html", {'re':read_obj})

def update(request,id):

    context ={}
    get_data = GeeksModel.objects.get(id = id)
    form = GeeksForm(request.POST or None,request.FILES or None,instance = get_data)
    if form.is_valid():
        form.save()
        
    context['val'] = form
    return render(request, "edit.html", context)
    
    
    
      
