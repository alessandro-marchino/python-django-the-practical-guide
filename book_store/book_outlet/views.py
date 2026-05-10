from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.db.models import Avg

from .models import Book

# Create your views here.
def index(req: HttpRequest) -> HttpResponse:
    books = Book.objects.all().order_by("title")
    return render(req, 'book_outlet/index.html', {
        "books": books,
        "total_number_of_books": books.count(),
        "average_rating": books.aggregate(Avg('rating'))
    })

def book_detail(req: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    return render(req, 'book_outlet/book_detail.html', book.__dict__)
