from django.shortcuts import render, redirect

# Sample data acting as a database
data = [
    {'id': 1, 'name': 'Aditya', 'age': 22},
    {'id': 2, 'name': 'Akshit', 'age': 33},
    {'id': 3, 'name': 'Kavya', 'age': 13},
]

def web(request):
    text = "This is from backend"
    return render(request, "home.html", context={'data': data, 'text': text})

def create_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        new_id = max(item['id'] for item in data) + 1
        data.append({'id': new_id, 'name': name, 'age': int(age)})
        return redirect(web)
    return render(request, "create.html")

def update_user(request):
    return render(request, "update.html")

