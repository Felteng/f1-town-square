from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home"),
    path("calendar/", views.calendar, name="calendar"),
    path("articles/", views.articles, name="articles")
]