from django.contrib import admin
from .models import Article, RaceEvent

# Register your models here.
admin.site.register(Article)
admin.site.register(RaceEvent)