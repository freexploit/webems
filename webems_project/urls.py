from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('globals.urls')),
    url(r'^emulations/*', include('emulations.urls')),
    url(r'^accounts/*', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
