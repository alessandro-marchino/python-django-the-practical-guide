from typing import Any
from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .forms import CommentForm

all_posts = []

# Create your views here.
class StartingPageView(ListView):
  template_name = 'blog/index.html'
  model = Post
  ordering = [ "-date", "pk" ]
  context_object_name = "posts"

  def get_queryset(self) -> QuerySet[Any]:
    return super().get_queryset()[:3]

class AllPostsView(ListView):
  template_name = 'blog/all-posts.html'
  model = Post
  ordering = [ "-date", "pk" ]
  context_object_name = "all_posts"

class SinglePostView(View):
  def get(self, req: HttpRequest, slug: str) -> HttpResponse:
    post = Post.objects.get(slug=slug)
    ctx = {
      "post": post,
      "post_tags": post.tags.all(),
      "comment_form": CommentForm()
    }

    return render(req, "blog/post-detail.html", ctx)

  def post(self, req: HttpRequest, slug:str) -> HttpResponse:
    post = Post.objects.get(slug=slug)
    comment_form = CommentForm(req.POST)
    if not comment_form.is_valid():
      ctx = {
        "post": post,
        "post_tags": post.tags.all(),
        "comment_form": comment_form
      }
      return render(req, "blog/post-detail.html", ctx)

    comment = comment_form.save(commit=False)
    comment.post = post
    comment.save()
    return HttpResponseRedirect(reverse("post-detail-page", args=[ slug ]))

