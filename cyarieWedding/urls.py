from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'cyarieWedding.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^wedding/', include('wedding.urls')),
                       url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'home/login.html'}),
                       url(r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'home/logout.html'}),
                       url(r'^$', include('home.urls')),
                       url(r'^rsvp/', include('rsvp.urls')),
                       )
