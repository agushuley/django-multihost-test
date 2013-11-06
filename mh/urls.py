from django.conf.urls import patterns, include, url
from django.contrib import admin

from .default import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'multihost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(..)/news/item/(\d+)/$', views.news_item, name="news_item"),
    url(r'^templates/$', views.templates, name="templates"),
)
