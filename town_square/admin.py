from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, RaceEvent

# Register your models here.
@admin.register(Article)
class articleAdmin(SummernoteModelAdmin):
  list_display = ('title', 'author', 'published', 'created_on')
  summernote_fields = ('body')
  prepopulated_fields = {'slug': ('title',)}

@admin.register(RaceEvent)
class calendarAdmin(SummernoteModelAdmin):
  list_display = ('location', 'start_date', 'event_name',)
  search_fields = ['location']
  prepopulated_fields = {'slug': ('event_name',)}

