from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('',
	
	url(r'emulation/(?P<pk>\d+)/view/$', 'emulations.views.view'),
    url(r'emulation/(?P<pk>\d+)/edit/$', 'emulations.views.edit'),
    url(r'emulation/(?P<pk>\d+)/delete/$', 'emulations.views.delete'),
    url(r'emulation/(?P<pk>\d+)/myemulations/$', 'emulations.views.myemulations'),
    url(r'emulation/(?P<pk>\d+)/remove_myemulations/$', 'emulations.views.remove_myemulations'),
)
