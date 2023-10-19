from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book


def index(request):
    books = Book.objects.all()
    
    context = {
        'books': books
    }

    return render(request, 'index.html', context)

def navbar(request):
    return render(request, 'navbar.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')