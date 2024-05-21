from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(
        request,
        "town_square/index.html"
    )


def calendar(request):
    return render(
        request,
        "town_square/calendar.html"
    )


def articles(request):
    return render(
        request,
        "town_square/articles.html"
    )