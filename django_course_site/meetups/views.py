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

def meetup_details(req: HttpRequest, meetup_slug: str) -> HttpResponse:
    selected_meetup = { 'title': 'A First Meetup', 'description': 'This is the first meetup!' }
    return render(req, 'meetups/meetup-details.html', {
        'meetup': selected_meetup
    })
