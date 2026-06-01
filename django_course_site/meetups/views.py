from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.

def index(req: HttpRequest) -> HttpResponse:
    meetups = Meetup.objects.all()
    return render(req, 'meetups/index.html', {
        'meetups': meetups
    })

def meetup_details(req: HttpRequest, meetup_slug: str) -> HttpResponse:
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if req.method == 'GET':
            form = RegistrationForm()
        else:
            form = RegistrationForm(req.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')

        return render(req, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': form
        })
    except Exception as exc:
        return render(req, 'meetups/meetup-details.html', {
            'meetup_found': False
        })

def confirm_registration(req: HttpRequest) -> HttpResponse:
    return render(req, 'meetups/registration-success.html')
