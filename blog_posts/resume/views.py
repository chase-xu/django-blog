from django.shortcuts import render
from django.http import HttpResponse
from .models import Experience, School
# Create your views here.

def resume(request):
    exps = Experience.objects.all().order_by('-start_date').values()
    schools = School.objects.all().order_by('-start_date').values()
    for obj in exps:
        obj['duty'] = obj['duty'].split('\n')

    context = {
        'exps': exps,
        'schools': schools
    }
    return render(request, 'resume.html', context)