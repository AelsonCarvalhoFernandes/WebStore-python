from django.shortcuts import render
from stock.models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'public/index.html', {'products': products})

def register(request):
    pass

def login(request):
    pass

def logout(request):
    pass
