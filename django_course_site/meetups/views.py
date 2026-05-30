from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(req: HttpRequest) -> HttpResponse:
    meetups = [
        { 'title': 'A First Meetup' },
        { 'title': 'A Second Meetup' }
    ]
    return render(req, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
