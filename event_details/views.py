from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import RaceEventDetail, RaceEventComment
from .forms import RaceCommentForm

# Create your views here.
def event_details(request, event_id):
    queryset = RaceEventDetail.objects.filter(race=event_id)
    event = get_object_or_404(queryset)
    race_distance = round(event.circuit_length * event.number_of_laps, 2)
    comments = event.comments.all()
    comment_count = comments.filter(approved=True).count()

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


def approve_comment(request, event_id, target_comment):
    """
    Approve an indiviual comment.

    **Context**

    ``comment``
    The single comment related to the comment.id targeted from the template.

    """
    comment = get_object_or_404(RaceEventComment, pk=target_comment)

    if request.user.is_superuser:
        comment.approved = True
        comment.save()

    return HttpResponseRedirect(reverse('event_details', args=[event_id]))


def delete_comment(request, event_id, target_comment):
    """
    Delete an individual comment.

    **Context**

    ``comment``
    The single comment related to the comment.id targeted from the template.

    """
    comment = get_object_or_404(RaceEventComment, pk=target_comment)
    
    if request.user == comment.author:
        comment.delete()

    return HttpResponseRedirect(reverse('event_details', args=[event_id]))


def edit_comment(request, event_id, target_comment):
    """
    Delete an individual comment.

    **Context**

    ``comment``
    The single comment related to the comment.id targeted from the template.

    """
    if request.method == "POST":
        comment = get_object_or_404(RaceEventComment, pk=target_comment)
        race_comment_form = RaceCommentForm(data=request.POST, instance=comment)
        if request.user == comment.author and race_comment_form.is_valid():
            comment = race_comment_form.save(commit=False)
            comment.approved = False
            comment.save()

    return HttpResponseRedirect(reverse('event_details', args=[event_id]))