from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Book

# Create your views here.
def index(req: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(req, 'book_outlet/index.html', {
        "books": books
    })
