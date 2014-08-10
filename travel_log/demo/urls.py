from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.template import add_to_builtins

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^travel_log/', include('travel_log.urls', namespace='travel_log')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^robots\.txt$',
                           TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)

add_to_builtins('django.templatetags.i18n')