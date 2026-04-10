from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound


challenges = {
    'january': 'Eat no chocolate for the entire month',
    'february': 'Walk for at least 20 minutes every day',
    'march': 'Learn Django for at least 20 minutes every day'
}


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    if month in challenges:
        return HttpResponse(challenges[month])
    return HttpResponseNotFound('This month is not supported')

def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    return HttpResponse(month)
