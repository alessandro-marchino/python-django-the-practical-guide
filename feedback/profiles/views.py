from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.files.uploadedfile import UploadedFile

from .forms import ProfileForm

# Create your views here.

def store_files(file: UploadedFile):
    with open("temp/file.pdf", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)



class CreateProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
          store_files(request.FILES["user_image"])
          return HttpResponseRedirect("/profiles")
        return render(request, "profiles/create_profile.html", {
            "form": form
        })
