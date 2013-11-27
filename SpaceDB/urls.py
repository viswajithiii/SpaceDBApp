from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SpaceDB.views.home', name='home'),
    # url(r'^SpaceDB/', include('SpaceDB.foo.urls')),
    url(r'^$','SpaceDB.views.home'),
    url(r'^astronomer/$', 'SpaceDB.views.astronomer'),
    url(r'^astronomer/(?P<id>\d+)/$', 'SpaceDB.views.oneastronomer'),
    url(r'^astronaut/$', 'SpaceDB.views.astronaut'),
    url(r'^astronaut/(?P<id>\d+)/$', 'SpaceDB.views.oneastronaut'),
    url(r'^planet/$','SpaceDB.views.planet'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
