from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404

from .models import Book

# Create your views here.
def index(req: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(req, 'book_outlet/index.html', {
        "books": books
    })

def book_detail(req: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    return render(req, 'book_outlet/book_detail.html', book.__dict__)
