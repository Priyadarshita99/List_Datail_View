from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class Schoollist(ListView):
    model=School
    context_object_name='schools'
    ordering=['Sname']                 #Sname will display alphabetically
    #queryset=School.objects.filter(pk=1)
    #template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'
    
class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
    
class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('Schoollist')
