from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class RaceEvent(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField()
    event_name = models.CharField(max_length=100, unique=True)
    event_image = CloudinaryField('Event image', default='event_placeholder')

    def __str__(self):
        return self.event_name
