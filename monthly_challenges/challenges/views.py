from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect


challenges = {
    'january': 'Eat no chocolate for the entire month',
    'february': 'Walk for at least 20 minutes every day',
    'march': 'Learn Django for at least 20 minutes every day',
    'april': 'Eat no chocolate for the entire month',
    'may': 'Walk for at least 20 minutes every day',
    'june': 'Learn Django for at least 20 minutes every day',
    'july': 'Eat no chocolate for the entire month',
    'august': 'Walk for at least 20 minutes every day',
    'september': 'Learn Django for at least 20 minutes every day',
    'october': 'Eat no chocolate for the entire month',
    'november': 'Walk for at least 20 minutes every day',
    'december': 'Learn Django for at least 20 minutes every day'
}


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    try:
        return HttpResponse(challenges[month])
    except:
        return HttpResponseNotFound('This month is not supported')


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    if month < 0 or month > 12:
        return HttpResponseNotFound('This month is not supported')

    months = list(challenges.keys())
    forward_month = months[month - 1]
    return HttpResponseRedirect(f"/challenges/{forward_month}")
