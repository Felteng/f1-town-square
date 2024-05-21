from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class RaceEvent(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField()
    event_name = models.CharField()
    event_image = CloudinaryField('image', default='event_placeholder')


# Code source: https://github.com/Code-Institute-Solutions/Django3blog/blob/75bd87f4439d678bee07c149383cf2d778c38a6f/11_messages/blog/models.py#L9-L25
class Article(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="articles"
        )
    body = models.TextField()
    article_image = CloudinaryField('image', default='t7ycznl8fsl6irkde9pa')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]