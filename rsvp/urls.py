from django.conf.urls import patterns, url
from rsvp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^submit/', views.rsvp, name='rsvp'),
                       )
