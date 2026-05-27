from typing import Any
from array import array

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
  @staticmethod
  def get_ctx(post: Post, comment_form: CommentForm, req: HttpRequest):
    return {
      "post": post,
      "post_tags": post.tags.all(),
      "post_comments": post.comments.all().order_by('-id'),
      "comment_form": comment_form,
      "saved_for_later": post.id in req.session.get('stored_posts', [])
    }

  def get(self, req: HttpRequest, slug: str) -> HttpResponse:
    post = Post.objects.get(slug=slug)
    ctx = SinglePostView.get_ctx(post, CommentForm(), req)

    return render(req, "blog/post-detail.html", ctx)

  def post(self, req: HttpRequest, slug:str) -> HttpResponse:
    post = Post.objects.get(slug=slug)
    comment_form = CommentForm(req.POST)
    if not comment_form.is_valid():
      ctx = SinglePostView.get_ctx(post, comment_form, req)
      return render(req, "blog/post-detail.html", ctx)

    comment = comment_form.save(commit=False)
    comment.post = post
    comment.save()
    return HttpResponseRedirect(reverse("post-detail-page", args=[ slug ]))

class ReadLaterView(View):
  def get(self, req: HttpRequest) -> HttpResponse:
    stored_posts = req.session.get('stored_posts', [])
    ctx = {
      'posts': Post.objects.filter(id__in=stored_posts),
      'has_posts': len(stored_posts) > 0
    }

    return render(req, 'blog/stored-posts.html', ctx)

  def post(self, req: HttpRequest) -> HttpResponse:
    stored_posts: array[int] = req.session.get('stored_posts', [])
    post_id = int(req.POST["post_id"])
    if post_id not in stored_posts:
      stored_posts.append(post_id)
    else:
      stored_posts.remove(post_id)
    req.session['stored_posts'] = stored_posts
    return HttpResponseRedirect('/')
