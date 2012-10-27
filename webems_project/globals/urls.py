from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('',
	url(r'^$', 'emulations.views.mine'),
	url(r'^all$', 'emulations.views.all'),
	url(r'^create$', 'emulations.views.create'),
	# url(r'^about/$', 'globals.views.about'),
)
