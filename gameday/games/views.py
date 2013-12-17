from django.views.generic import ListView

from games.models import Game

from datetime import date

class IndexView(ListView):
    context_object_name = 'games'
    queryset = Game.objects.filter(date=date.today())
    template_name = 'index.html'
    
