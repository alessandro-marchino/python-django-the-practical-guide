from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View

# Create your views here.


class CreateProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "profiles/create_profile.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        image = request.FILES["image"]
        print(image)
        return HttpResponseRedirect("/profiles")
