from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def project(request):
    projects = Project.objects.all().order_by('-start_date').values()
    for obj in projects:
        obj['description'] = obj['description'].split('\n')
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)
