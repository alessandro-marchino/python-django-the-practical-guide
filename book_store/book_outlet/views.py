from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(req: HttpRequest) -> HttpResponse:
    return render(req, 'book_outlet/index.html')
