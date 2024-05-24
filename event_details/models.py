from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from town_square.models import RaceEvent

# Create your models here.
class RaceEventDetail(models.Model):
    race = models.OneToOneField(
        RaceEvent, on_delete=models.CASCADE, related_name='event_details'
    )
    event_info = models.TextField()
    circuit_image = CloudinaryField('Circuit layout', default='circuit_default')
    circuit_name = models.CharField()
    circuit_info = models.TextField()