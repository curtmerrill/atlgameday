from datetime import date

from django.views.generic import ListView
from django.views.decorators.cache import cache_page

from games.models import Game

class CacheViewMixin(object):
    cache_timeout = 60

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheViewMixin, self).dispatch)(*args, **kwargs)


class IndexView(CacheViewMixin, ListView):
    cache_timeout = 60*30
    context_object_name = 'games'
    queryset = Game.objects.filter(date=date.today())
    template_name = 'index.html'
    
