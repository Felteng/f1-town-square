from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import RaceEvent


# Register your models here.
@admin.register(RaceEvent)
class calendarAdmin(SummernoteModelAdmin):
    list_display = ('location', 'start_date', 'event_name',)
    search_fields = ['location']
