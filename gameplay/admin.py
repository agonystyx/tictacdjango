from django.contrib import admin

from .models import Game, Move

#admin.site.register(Game)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
  list_display=('id', 'first_player', 'second_player', 'status')
  list_editable=('status',) #must add comma otherwise python won't know tuple


admin.site.register(Move)
