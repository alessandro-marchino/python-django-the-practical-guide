from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def review(req: HttpRequest) -> HttpResponse:
    if req.method == 'GET':
      return render(req, "reviews/review.html", {
          'has_error': False
       })
    entered_username = req.POST['username']
    if entered_username == "":
       return render(req, "reviews/review.html", {
          'has_error': True
       })
    print(entered_username)
    return HttpResponseRedirect('/thank-you')

def thank_you(req: HttpRequest) -> HttpResponse:
   return render(req, "reviews/thank-you.html")
