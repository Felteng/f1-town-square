from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(
        request,
        "town_square/index.html"
    )