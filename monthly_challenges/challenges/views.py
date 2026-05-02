from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    'december': None
}

def index(request: HttpRequest) -> HttpResponse:
    months = list(challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse('month-challenge', args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    try:
        challenge_text = challenges[month]
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound('<h1>This month is not supported</h1>')


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    months = list(challenges.keys())
    if month < 0 or month > len(months):
        return HttpResponseNotFound('<h1>This month is not supported<h1>')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
