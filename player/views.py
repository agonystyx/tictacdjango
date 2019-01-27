from django.shortcuts import render
from gameplay.models import Game

def home(request):
  #return render(request, "player/home.html")

  # return render(
  #   request,
  #   "player/home.html",
  #   {'ngames': Game.objects.count()}
  #   )

  # gather all games where
  # the current user is next to play
  # # games_first_player = Game.objects.filter(
  # #   first_player = request.user,
  # #   status='F'
  # # )
  # # games_second_player = Game.objects.filter(
  # #   second_player = request.user,
  # #   status='S'
  # # )
  # #
  # # all_my_games = list(games_first_player) + \
  # #                list(games_second_player)
  # #
  # # n_games = len(all_my_games)
  # #
  # # game_str = "game" if (n_games == 1) else  "games"
  #
  # return render(
  #   request,
  #   "player/home.html",
  #
  #   { 'n_games': n_games,
  #   'game_str':game_str,
  #   'games' : all_my_games}
  # )

  all_my_games = Game.objects.games_for_user(request.user)
  active_games = all_my_games.active()
  n_games = len(active_games)


  template = "player/home.html"
  context = { 'n_games': n_games,
              'game_str': "game" if (n_games == 1) else  "games",
              'games' : active_games
  }

  return render(request, template, context)
