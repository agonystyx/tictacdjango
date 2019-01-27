#from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
#  return HttpResponse("Hello, World!")
  return render(request, "tictactoe/welcome.html")
