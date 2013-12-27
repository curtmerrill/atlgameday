from datetime import date

from django.views.generic import ListView
from django.core.cache import cache, get_cache

from games.models import Game

class IndexView(ListView):
    context_object_name = 'games'
    template_name = 'index.html'

    def get_queryset(self):
        if not cache.get('games_today'):
            cache.set('games_today', Game.objects.filter(date=date.today()), 60*30)
        return cache.get('games_today')

