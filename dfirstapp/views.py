from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    return render(request, 'home.html')

def studentprof(request):
    return render(request, 'home.html')

def teamprof(request):
    return render(request, 'home.html')

def match(request):
    strmessage =''
    if request.method=='GET':
        # return HttpResponse(strmessage)
        return None

    else:

        # return HttpResponse(strmessage)
        return None
def contact(request):
    return render(request, 'home.html')