from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import RaceEventDetail, RaceEventComment
from .forms import RaceCommentForm


# Create your views here.
def event_details(request, event_id):
    queryset = RaceEventDetail.objects.filter(race=event_id)
    event = get_object_or_404(queryset)
    race_distance = round(event.circuit_length * event.number_of_laps, 2)
    comments = event.comments.all()
    comment_count = comments.filter(approved=True).count()

    # https://stackoverflow.com/a/57682143: forcing https for images.
    event.event_hero_image.url_options.update({'secure':True})
    event.race.event_circuit.url_options.update({'secure':True})

    if request.method == "POST":
        race_comment_form = RaceCommentForm(data=request.POST)
        if race_comment_form.is_valid():
            comment = race_comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Your comment has been added.")
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong, your comment could not be added.")

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
        messages.add_message(request, messages.SUCCESS, "Comment approved successfully.")
    else:
        messages.add_message(request, messages.ERROR, "Comment could not be approved, are you a site admin?")
    
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
        messages.add_message(request, messages.SUCCESS, "Comment deleted successfully.")
    else:
        messages.add_message(request, messages.ERROR, "Comment could not be deleted, are you the author?")

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
        race_comment_form = RaceCommentForm(
            data=request.POST, instance=comment
            )
        if request.user == comment.author and race_comment_form.is_valid():
            comment = race_comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment edited successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Comment could not be edited, are you the author?")

    return HttpResponseRedirect(reverse('event_details', args=[event_id]))
