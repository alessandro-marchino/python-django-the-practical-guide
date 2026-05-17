from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review

# Create your views here.
def review(req: HttpRequest) -> HttpResponse:
    if req.method == 'GET':
      form = ReviewForm()
      return render(req, "reviews/review.html", {
          "form": form
       })

    form = ReviewForm(req.POST)
    if not form.is_valid():
       return render(req, "reviews/review.html", {
          "form": form
       })
    review = Review(user_name=form.cleaned_data["user_name"], review_text=form.cleaned_data["review_text"], rating=form.cleaned_data["rating"])
    review.save()
    return HttpResponseRedirect('/thank-you')

def thank_you(req: HttpRequest) -> HttpResponse:
   return render(req, "reviews/thank-you.html")
