from django.shortcuts import render

def index(request):
    return render(request, 'public/index.html')

def register(request):
    pass

def login(request):
    pass

def logout(request):
    pass
