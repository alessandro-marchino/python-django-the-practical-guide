from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def starting_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/index.html')

def posts(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/all-posts.html')

def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    return render(request, 'blog/post-detail.html')
