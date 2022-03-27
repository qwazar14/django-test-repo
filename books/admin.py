from django.contrib import admin
from books.models import Book, Author, Authored, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Authored)
admin.site.register(Genre)
