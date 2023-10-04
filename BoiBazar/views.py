from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def navbar(request):
    return render(request, 'navbar.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')