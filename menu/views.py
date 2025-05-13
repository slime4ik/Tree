from django.shortcuts import render
from menu.models import Menu
# Create your views here.
def menu_view(request):
    return render(request, 'base.html')

def food_view(request):
    return render(request, 'base.html')

def citruse_view(request):
    return render(request, 'base.html')

def lime_view(request):
    return render(request, 'base.html')

def orange_view(request):
    return render(request, 'base.html')

# def drink_view(request):
#     return render(request, 'base.html')

# def nonalcohol_view(request):
#     return render(request, 'base.html')

# def alcohol_view(request):
#     return render(request, 'base.html')
