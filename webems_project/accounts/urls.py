from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('',
	
	url(r'^login/$', 'accounts.views.accounts'),
	# url(r'^signup/$', 'accounts.views.signup'),
)
