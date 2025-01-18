from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')
    # return HttpResponse("Hello from home")

def about(request):
    return render(request,'about.html')

def services(request):
    return HttpResponse("Hello from services")