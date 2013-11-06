from django.conf.urls import patterns, include, url
from . import views

__author__ = 'andriyg'

urlpatterns = patterns('',
    url(r'^(..)/ni/(\d+)/$', views.news_item, name="news_item"),
    url(r'^templates/$', views.templates, name="templates"),
)
