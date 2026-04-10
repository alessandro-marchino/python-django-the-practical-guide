from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def january(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Eat no chocolate for the entire month")


def february(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Walk for at least 20 minutes every day")
