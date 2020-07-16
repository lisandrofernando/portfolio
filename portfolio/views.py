from django.shortcuts import render
from .models import Project
def homepage(request):
    Projects = Project.objects.all()
    return render(request,'portfolio/homepage.html', {'projects': Projects})

