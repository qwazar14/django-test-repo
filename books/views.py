
from django.shortcuts import render

from books.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'title': 'Книги', 'books': books})


def add(request):
    pass

def about(request):
    pass

