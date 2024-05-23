from django.shortcuts import render, get_object_or_404
from .models import DetailedRaceEvent

# Create your views here.
def event_details(request, event_id):
    queryset = DetailedRaceEvent.objects.filter(race=event_id)
    event = get_object_or_404(queryset)

    return render(
        request,
        'event_details/event_details.html',
        {
            'event': event,
        }
    )