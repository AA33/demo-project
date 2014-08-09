from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^travel_log/', include('travel_log.urls', namespace='travel_log')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^robots\.txt$',
                           TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)