from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import RaceEventDetail

# Register your models here.
@admin.register(RaceEventDetail)
class articleAdmin(SummernoteModelAdmin):
  list_display = ('race')
  summernote_fields = ('event_info')