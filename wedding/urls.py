from django.conf.urls import patterns, url
from wedding import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^invite/', views.invite_people, name='invite_people'),
                       )