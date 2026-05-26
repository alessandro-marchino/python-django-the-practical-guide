from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CommentForm

all_posts = []

# Create your views here.
class StartingPageView(ListView):
  template_name = 'blog/index.html'
  model = Post
  ordering = [ "-date", "pk" ]
  context_object_name = "posts"

  def get_queryset(self):
    return super().get_queryset()[:3]

class AllPostsView(ListView):
  template_name = 'blog/all-posts.html'
  model = Post
  ordering = [ "-date", "pk" ]
  context_object_name = "all_posts"

class SinglePostView(DetailView):
  template_name = "blog/post-detail.html"
  model = Post
  context_object_name = "post"

  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx["post_tags"] = self.get_object().tags.all()
    ctx["comment_form"] = CommentForm()
    return ctx
