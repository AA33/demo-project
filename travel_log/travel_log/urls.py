__author__ = 'abhishekanurag'

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from travel_log import views

urlpatterns = patterns('',

                       # /travel_log
                       url(r'^$', views.index, name='index'),
                       # /travel_log/userlogin
                       url(r'^userlogin/$', views.userlogin, name='userlogin'),
                       # /travel_log/userlogout
                       url(r'^userlogout/$', views.userlogout, name='userlogout'),
                       # /travel_log/signup
                       url(r'^signup/$', views.signup, name='signup'),
                       # /travel_log/home
                       url(r'^home/$', views.home, name='home'),
                       # /travel_log/<trip_id>/view
                       url(r'^(?P<trip_id>\d+)/view/$', views.trip_view, name='view'),
                       # /travel_log/edit : For new trips
                       url(r'^edit/$', views.trip_edit, name='edit'),
                       # /travel_log/<trip_id>/edit
                       url(r'^(?P<trip_id>\d+)/edit/$', views.trip_edit, name='edit'),
                       # /travel_log/<trip_id>/delete
                       url(r'^(?P<trip_id>\d+)/delete/$', views.trip_delete, name='delete'),

)
