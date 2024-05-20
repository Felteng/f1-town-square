from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
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