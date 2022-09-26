from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic

from .models import detiles_form

class creat_view(generic.CreateView):
    model = detiles_form
    fields = '__all__'
    template_name = 'create.html'
    success_url = 'http://127.0.0.1:8000/view/creat'
    
class list_view(ListView):
    
    model = detiles_form
    fields = '__all__'
    template_name = 'lis.html'
    
class update_view(generic.UpdateView):
    
    model = detiles_form
    fields = '__all__'
    template_name = 'update_form.html'
    success_url = 'http://127.0.0.1:8000/view/lis'
    
class del_view(generic.DeleteView):
    
    model = detiles_form
    fields = '__all__'
    template_name = 'delete_view.html'
    success_url = 'http://127.0.0.1:8000/view/lis'
    
    
    
