from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
# Create your views here.

def signup(request):
    form = StudentProfileForm
    return render(request, 'home.html', {
        'form': form
    })

def studentprof(request):
    return render(request, 'home.html')

def teamprof(request):
    return render(request, 'home.html')

def match(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'home.html')
