from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Meetup

# Create your views here.

def index(req: HttpRequest) -> HttpResponse:
    meetups = Meetup.objects.all()
    return render(req, 'meetups/index.html', {
        'meetups': meetups
    })

def meetup_details(req: HttpRequest, meetup_slug: str) -> HttpResponse:
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(req, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup
        })
    except Exception as exc:
        return render(req, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
