# views.py
from django.shortcuts import render,HttpResponse

def web(request):
    data = [
        {'name' : 'Aditya', 'age':22},
        {"name":"Akshit","age":33}
    ] 
    return render(request,"home.html", context = {'data':data})
#with the help of this context we can send out data from backend to our webpage 
