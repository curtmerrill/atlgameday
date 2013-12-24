from datetime import date

from django.views.generic import ListView

from games.models import Game

class IndexView(CacheViewMixin, ListView):
    context_object_name = 'games'
    queryset = Game.objects.filter(date=date.today())
    template_name = 'index.html'
    
