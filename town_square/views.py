from django.shortcuts import render, get_object_or_404
from .models import RaceEvent
from datetime import timedelta, datetime


# Create your views here.
def home_page(request):
    """
    Fetch all RaceEvent objects and loop through them
    until the closest upcoming event is iterated over.

    Save every event before the upcoming one in the 'previous' array
    so we can reverse and slice it to get the past 3 events to pass
    to the template as 'previous_events'.

    **Context**

    ``upcoming_event``
    The closest event (By date) to current date
    of :model:`town_square.RaceEvent`

    ``previous_events``
    The 3 closest instances (By date) to the upcoming event
    of :model:`town_square.RaceEvent`

    **Template:**

    :template:`town_square/index.html`
    """
    events = RaceEvent.objects.all()
    previous = []

    for event in events:
        # https://stackoverflow.com/a/57682143: forcing https for image.
        event.event_circuit.url_options.update({'secure': True})

        event.end_date = event.start_date + timedelta(days=2)
        if (
            event.start_date + timedelta(days=3) >
            datetime.date(datetime.now())
        ):
            upcoming_event = event
            break
        previous.append(event)

    previous.reverse()
    previous_events = previous[:3]

    return render(
        request,
        "town_square/index.html",
        {
            "previous_events": previous_events,
            "upcoming_event": upcoming_event,
        }
    )


def calendar(request):
    """
    Display the season calendar events.

    Fetch all RaceEvent objects to loop through them
    to force the circuit image to use https protocol
    and to add .end_date before rendering the template.

    **Context**

    ``events``
    All instances of :model:`town_square.RaceEvent`

    **Template:**

    :template:`town_square/calendar.html`
    """
    events = RaceEvent.objects.all()

    for event in events:
        # https://stackoverflow.com/a/57682143: forcing https for images.
        event.event_circuit.url_options.update({'secure': True})

        event.end_date = event.start_date + timedelta(days=2)

    return render(
        request,
        "town_square/calendar.html",
        {
            "events": events,
        }
    )
