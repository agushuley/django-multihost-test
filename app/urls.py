# Copyright (c) 2013 Andriy Gushuley
# Licensed under the terms of the MIT License (see LICENSE.txt)

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url( r'^admin/doc/', include( 'django.contrib.admindocs.urls' ) ),
   url( r'^admin/', include( admin.site.urls ) ),

    # Example:
    # (r'^app/', include('app.foo.urls')),
)
