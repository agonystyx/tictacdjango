from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gameplay.models import Game

@login_required
def home(request):

  all_my_games = Game.objects.games_for_user(request.user)
  active_games = all_my_games.active()
  n_games = len(active_games)


  template = "player/home.html"
  context = { 'n_games': n_games,
              'game_str': "game" if (n_games == 1) else  "games",
              'games' : active_games
  }

  return render(request, template, context)
