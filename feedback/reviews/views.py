from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def review(req: HttpRequest) -> HttpResponse:
    return render(req, "reviews/review.html")
