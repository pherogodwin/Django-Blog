from django.shortcuts import render

from .models import Game


def games_home(request):
    games = Game.objects.all()

    context = {
        "games": games,
    }
    return render(request, "games/games_home.html", context)


def wallet(request):
    return render(request, "games/wallet.html")