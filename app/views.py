from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView

class Schoollist(ListView):
    model=School
    context_object_name='schools'
    ordering=['Sname']                 #Sname will display alphabetically
    #queryset=School.objects.filter(pk=1)
    #template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'
