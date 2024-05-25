from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class RaceEvent(models.Model):
    start_date = models.DateField()
    location = models.CharField(max_length=32)
    event_name = models.CharField(max_length=100, unique=True)
    event_circuit = CloudinaryField('Event circuit', default='event_placeholder')

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return self.location + ": " + self.event_name
