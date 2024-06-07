from django.shortcuts import render, get_object_or_404, reverse, Http404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import RaceEventDetail, RaceEventComment
from .forms import RaceCommentForm


# Create your views here.
def event_details(request, event_id):
    """
    Display the indiviual :model:`event_details.RaceEventDetail`
    related to the id of :model:`town_square.RaceEvent` selected from
    the calendar page.

    **Context**

    ``event``
        The instance of :model:`event_details.RaceEventDetail` with
        the one-to-one relation to the :model:`town_square.RaceEvent`
        identified by the event_id arg.
    ``race_distance``
        Product of queried event.circuit_length and event.number_of_laps.
    ``comments``
        All comments related to the datailed event.
    ``comment_count``
        The amount of related comments with an approved status of True.
    ``race_comment_form``
        An instance of :form:`event_details.RaceCommentForm`.

    **Template:**
    :template:`event_details/event_details.html`
    """
    queryset = RaceEventDetail.objects.filter(race=event_id)
    event = get_object_or_404(queryset)
    race_distance = round(event.circuit_length * event.number_of_laps, 2)
    comments = event.comments.all()
    comment_count = comments.filter(approved=True).count()

    # https://stackoverflow.com/a/57682143: forcing https for images.
    event.event_hero_image.url_options.update({'secure': True})
    event.race.event_circuit.url_options.update({'secure': True})

    if request.method == "POST":
        race_comment_form = RaceCommentForm(data=request.POST)
        if race_comment_form.is_valid():
            comment = race_comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your comment has been added."
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Something went wrong, your comment could not be added."
            )

    race_comment_form = RaceCommentForm()

    return render(
        request,
        'event_details/event_details.html',
        {
            'event': event,
            'race_distance': race_distance,
            'comments': comments,
            'comment_count': comment_count,
            'comment_form': race_comment_form,
        }
    )


# Decorator taken from: https://stackoverflow.com/a/12003808
@user_passes_test(
    lambda u: u.is_superuser, login_url="/not_an_admin",
    redirect_field_name=None
)
def approve_comment(request, event_id, target_comment):
    """
    Approve an indiviual comment if user passes the superuser check.

    If the check returns false the user is redirected to 404 /not_an_admin

    **Context**

    ``comment``
    The single comment related to the comment.id targeted from the template.

    """
    comment = get_object_or_404(RaceEventComment, pk=target_comment)
    comment.approved = True
    comment.save()
    messages.add_message(
        request,
        messages.SUCCESS,
        "Comment approved successfully."
    )
    return HttpResponseRedirect(reverse('event_details', args=[event_id]))


@login_required
def delete_comment(request, event_id, target_comment):
    """
    Delete an individual comment.

    Raise 404 if the query fails.

    **Context**

    ``comment``
    The single comment related to the comment.id targeted from the template.

    """
    try:
        comment = get_object_or_404(
            RaceEventComment,
            pk=target_comment,
            author=request.user
        )
    except Http404:
        raise Http404("Can't delete the comment.. Are you the author?")

    comment.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        "Comment deleted successfully."
        )
    return HttpResponseRedirect(reverse('event_details', args=[event_id]))


@login_required
def edit_comment(request, event_id, target_comment):
    """
    Delete an individual comment.

    Only attempt comment query if the comment form is valid
    to avoid unnecessary query requests. If the query fails
    raise 404.

    **Context**

    ``comment``
    The single comment related to the comment.id targeted from the template.

    """
    if request.method == "POST":
        race_comment_form = RaceCommentForm(data=request.POST)
        if race_comment_form.is_valid():
            try:
                comment = get_object_or_404(
                    RaceEventComment,
                    pk=target_comment,
                    author=request.user
                )
            except Http404:
                raise Http404("Can't edit the comment.. Are you the author?")

            race_comment_form = RaceCommentForm(
                data=request.POST, instance=comment
            )
            comment = race_comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Comment edited successfully."
            )

    return HttpResponseRedirect(reverse('event_details', args=[event_id]))
