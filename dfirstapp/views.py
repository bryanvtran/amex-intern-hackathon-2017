from django.shortcuts import render

# Create your views here.

def showhome(request):
    return render(request, 'home.html')