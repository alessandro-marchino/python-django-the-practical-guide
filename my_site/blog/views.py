from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from datetime import date
from .models import Post

all_posts = []

def get_date(post) -> date:
    return post['date']

# Create your views here.
def starting_page(request: HttpRequest) -> HttpResponse:
  latest_posts = Post.objects.all().order_by("-date")[:3]
  return render(request, 'blog/index.html', {
    "posts": latest_posts
  })

def posts(request: HttpRequest) -> HttpResponse:
  return render(request, 'blog/all-posts.html', {
    "all_posts": Post.objects.all().order_by("-date")
  })

def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
  identified_post = get_object_or_404(Post, slug=slug)

  return render(request, 'blog/post-detail.html', {
    "post": identified_post
  })
