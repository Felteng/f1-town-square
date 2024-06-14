from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from town_square.models import RaceEvent


# Create your models here.
class RaceEventDetail(models.Model):
    """
    Sets an entry of race event details to one to one related
    :model:`town_square.RaceEvent`.
    """
    race = models.OneToOneField(
        RaceEvent, on_delete=models.CASCADE, related_name='event_details'
    )
    event_hero_image = CloudinaryField(
        'Hero image', default='image/upload/v1716558951/checkered-flags.svg'
        )
    event_info = models.TextField()
    circuit_name = models.CharField(max_length=70)
    circuit_length = models.FloatField(default=0)
    number_of_laps = models.PositiveIntegerField(default=0)
    lap_record = models.CharField(
        'Lap record (x:xx.xxx)', max_length=8, default='x:xx.xxx'
        )

    def __str__(self):
        return self.race.location + ": " + self.race.event_name


# Model approach from: https://github.com/Code-Institute-Solutions/Django3blog/blob/75bd87f4439d678bee07c149383cf2d778c38a6f/12_final_deployment/blog/models.py#L34-L47  # noqa
class RaceEventComment(models.Model):
    """
    Stores a single comment entry related to
    :model:`event_details.RaceEventDetail` and :model:`auth.User`.
    """
    event = models.ForeignKey(
        RaceEventDetail, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='event_comments'
    )
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.comment
