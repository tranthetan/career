from django.shortcuts import render

def index(request):
    return render(request, 'login.html')

def login(request):
    return render()

def logout(request):
    return render()