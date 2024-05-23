from django.shortcuts import render, get_object_or_404
from .models import RaceEvent

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

