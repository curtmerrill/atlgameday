from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# from django.views.decorators.cache import cache_page

from games.views import IndexView

urlpatterns = patterns('',
    (r'^/?$', IndexView.as_view()),
    # (r'^about/?$', cache_page(TemplateView.as_view(template_name="about.html"), 60*120)),
    (r'^about/?$', TemplateView.as_view(template_name="about.html")),
)
