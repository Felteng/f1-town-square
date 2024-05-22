from django.shortcuts import render
from .models import RaceEvent, Article

# Create your views here.
def home_page(request):
    return render(
        request,
        "town_square/index.html"
    )


def calendar(request):
    queryset = RaceEvent.objects.all()
    events = queryset.order_by("start_date")
    return render(
        request,
        "town_square/calendar.html",
        {
            'events': events,
        }
    )


def articles(request):
    return render(
        request,
        "town_square/articles.html"
    )