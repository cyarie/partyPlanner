from django.conf.urls import patterns, url
from wedding import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^invite/', views.invite, name='invite'),
                       url(r'^invitations/', views.invitations, name='invitations'),
                       )