from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from games.views import IndexView

urlpatterns = patterns('',
    (r'^/?$', IndexView.as_view()),
    (r'^about/?$', TemplateView.as_view(template_name="about.html")),
)
