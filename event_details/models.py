from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from town_square.models import RaceEvent

# Create your models here.
class RaceEventDetail(models.Model):
    race = models.OneToOneField(
        RaceEvent, on_delete=models.CASCADE, related_name='event_details'
    )
    event_hero_image = CloudinaryField('Hero image', default="image/upload/v1716558951/checkered-flags.svg")
    event_info = models.TextField()
    circuit_name = models.CharField()
    circuit_length = models.FloatField(default=0)
    number_of_laps = models.PositiveIntegerField(default=0)
    lap_record = models.CharField('Lap record (x:xx.xxx)', max_length=8, default="x:xx.xxx")
