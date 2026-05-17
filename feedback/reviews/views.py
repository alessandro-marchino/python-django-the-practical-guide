from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

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

def thank_you(req: HttpRequest) -> HttpResponse:
   return render(req, "reviews/thank-you.html")
