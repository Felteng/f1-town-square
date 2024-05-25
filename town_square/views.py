from django.shortcuts import render, get_object_or_404
from .models import RaceEvent
from datetime import timedelta

# Create your views here.
def home_page(request):
    return render(
        request,
        "town_square/index.html"
    )


def calendar(request):
    queryset = RaceEvent.objects.all()
    events = queryset.order_by("start_date")

    for event in events:
        event.end_date = event.start_date + timedelta(days=2)

    return render(
        request,
        "town_square/calendar.html",
        {
            'events': events,
        }
    )

