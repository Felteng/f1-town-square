from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from town_square.models import RaceEvent

# Create your models here.
class DetailedRaceEvent(models.Model):
    race = models.OneToOneField(
        RaceEvent, on_delete=models.CASCADE, related_name='event_details'
    )
    event_info = models.TextField()