from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.files.uploadedfile import UploadedFile

# Create your views here.

def store_files(file: UploadedFile):
    with open("temp/file.pdf", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)



class CreateProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "profiles/create_profile.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        image = request.FILES["image"]
        store_files(image)
        return HttpResponseRedirect("/profiles")
