from typing import Any, Dict

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.http import HttpResponse, HttpRequest

from .models import Review
from .forms import ReviewForm

# Create your views here.

class ReviewView(CreateView):
  model = Review
  form_class = ReviewForm
  template_name = "reviews/review.html"
  success_url = "/thank-you"

class ThankYouView(TemplateView):
  template_name = "reviews/thank-you.html"

  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context["message"] = "This works!"
    return context

class ReviewsListView(ListView):
  template_name = "reviews/review-list.html"
  model = Review
  context_object_name = "reviews"

class SingleReviewView(DetailView):
  template_name = "reviews/single-review.html"
  model = Review
  context_object_name = "review"

class AddFavoriteView(View):
  def post(self, req: HttpRequest) -> HttpResponse:
    review_id = req.POST["review_id"]
    Review.objects.get(pk=review_id)

