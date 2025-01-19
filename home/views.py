# views.py
from django.shortcuts import render,HttpResponse

def web(request):
    return render(request,"home.html")
