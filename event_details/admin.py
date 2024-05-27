from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import RaceEventDetail, RaceEventComment

# Register your models here.
@admin.register(RaceEventDetail)
class articleAdmin(SummernoteModelAdmin):
  list_display = ('race', 'circuit_name')
  summernote_fields = ('event_info')

@admin.register(RaceEventComment)
class commentAdmin(SummernoteModelAdmin):
  list_display = ('comment', 'author', 'approved')
  list_filter = ('approved',)
  