from django.shortcuts import render


def home(request):
    title = "Home page"
    heading = "Bienvenue sur mon site"
    return render(
        request,
        "events/home.html",
        {"title": title, "h1": heading},
    )
