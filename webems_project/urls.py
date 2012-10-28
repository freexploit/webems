from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('globals.urls')),
    url(r'^emulations/*', include('emulations.urls')),
    url(r'emulation/(?P<pk>\d+)/view/$', 'emulations.views.view'),
    url(r'emulation/(?P<pk>\d+)/edit/$', 'emulations.views.edit'),
    url(r'emulation/(?P<pk>\d+)/delete/$', 'emulations.views.delete'),
    url(r'emulation/(?P<pk>\d+)/myemulations/$', 'emulations.views.myemulations'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
