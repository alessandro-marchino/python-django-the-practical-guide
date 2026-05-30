from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(req: HttpRequest) -> HttpResponse:
    meetups = [
        { 'title': 'A First Meetup', 'location': 'New York', 'slug': 'a-first-meetup' },
        { 'title': 'A Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup' }
    ]
    return render(req, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
