from django.shortcuts import render
from django.http  import HttpResponse
from .models import Project

# Create your views here.
def welcome(request):
    projects = Project.objects.all()
    print(projects)
    return render(request,'home.html',{ "projects":projects})
