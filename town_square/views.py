from django.shortcuts import render, get_object_or_404
from .models import RaceEvent
from datetime import timedelta, datetime


# Create your views here.
def home_page(request):
    """
    Fetch all RaceEvent objects and loop through them
    until the closest upcoming event iterated over.

    Save every event before the upcoming one in the 'previous' array
    so we can reverse and slice it to get the past 3 events to pass
    to the template as 'previous_events'.

    """
    events = RaceEvent.objects.all()
    previous = []

    for event in events:
        # https://stackoverflow.com/a/57682143: forcing https for image.
        event.event_circuit.url_options.update({'secure':True})

        event.end_date = event.start_date + timedelta(days=2)
        if event.start_date + timedelta(days=3) >= datetime.date(datetime.now()):
            upcoming_event = event
            break
        previous.append(event)

    previous.reverse()
    previous_events = previous[:3]

    return render(
        request,
        "town_square/index.html",
        {
            "upcoming_event": upcoming_event,
            "previous_events": previous_events,
        }
    )


def calendar(request):
    events = RaceEvent.objects.all()

    for event in events:
        event.event_circuit.url_options.update({'secure':True})
        event.end_date = event.start_date + timedelta(days=2)

    return render(
        request,
        "town_square/calendar.html",
        {
            "events": events,
        }
    )

