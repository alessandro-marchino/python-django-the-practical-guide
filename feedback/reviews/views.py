from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def review(req: HttpRequest) -> HttpResponse:
    if req.method == 'GET':
      return render(req, "reviews/review.html")
    entered_username = req.POST['username']
    print(entered_username)
    return HttpResponseRedirect('/thank-you')

def thank_you(req: HttpRequest) -> HttpResponse:
   return render(req, "reviews/thank-you.html")
