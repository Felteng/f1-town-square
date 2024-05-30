from django.urls import path
from . import views


urlpatterns = [
    path("<int:event_id>/", views.event_details, name="event_details"),
    path("<int:event_id>/approve_comment/<int:target_comment>", views.approve_comment, name="comment_approve"),
    path("<int:event_id>/delete_comment/<int:target_comment>", views.delete_comment, name="comment_delete"),
]