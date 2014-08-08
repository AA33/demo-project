from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^travel_log/', include('travel_log.urls', namespace='travel_log')),
                       url(r'^admin/', include(admin.site.urls)),
)