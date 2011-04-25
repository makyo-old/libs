from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('jnsqlibs.library.views',
    (r'^$', 'list_libraries'),
    (r'^library/(?P<library>[a-zA-Z\-]+)/$', 'show_library'),
    (r'^admin/', include(admin.site.urls)),

    (r'^(?P<library>[a-zA-Z\-]+)/$', 'use_library'),
    (r'^(?P<library>[a-zA-Z\-]+)/(?P<version>[^\\]+)/$', 'use_library'),
)
