from typing import Any, Dict

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Review
from .forms import ReviewForm

# Create your views here.

class ReviewView(View):
  def get(self, req: HttpRequest) -> HttpResponse:
    form = ReviewForm()
    return render(req, "reviews/review.html", {
      "form": form
    })

  def post(self, req: HttpRequest) -> HttpResponse:
    form = ReviewForm(req.POST)
    if not form.is_valid():
      return render(req, "reviews/review.html", {
        "form": form
      })
    form.save()
    return HttpResponseRedirect('/thank-you')

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

class SingleReviewView(TemplateView):
  template_name = "reviews/single-review.html"

  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context["review"] = Review.objects.get(pk=kwargs["id"])
    return context
