from django.shortcuts import render, get_object_or_404
from .models import RaceEventDetail

# Create your views here.
def event_details(request, event_id):
    queryset = RaceEventDetail.objects.filter(race=event_id)
    event = get_object_or_404(queryset)
    race_distance = round(event.circuit_length * event.number_of_laps, 2)

    return render(
        request,
        'event_details/event_details.html',
        {
            'event': event,
            'race_distance': race_distance,
        }
    )