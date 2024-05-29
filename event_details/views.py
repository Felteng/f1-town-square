from django.shortcuts import render, get_object_or_404
from .models import RaceEventDetail, RaceEventComment
from .forms import RaceCommentForm

# Create your views here.
def event_details(request, event_id):
    queryset = RaceEventDetail.objects.filter(race=event_id)
    event = get_object_or_404(queryset)
    race_distance = round(event.circuit_length * event.number_of_laps, 2)
    comments = event.comments.all()
    comment_count = comments.count()

    if request.method == "POST":
        race_comment_form = RaceCommentForm(data=request.POST)
        if race_comment_form.is_valid():
            comment = race_comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()

    race_comment_form = RaceCommentForm()

    return render(
        request,
        'event_details/event_details.html',
        {
            'event': event,
            'comments': comments,
            'race_distance': race_distance,
            'comment_form': race_comment_form,
            'comment_count': comment_count,
        }
    )