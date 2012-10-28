from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, TemplateView

urlpatterns = patterns('',
	
	url(r'^$', 'accounts.views.accounts'),
	url(r'^signin/$', 'accounts.views.signin'),
	url(r'^signup/$', 'accounts.views.signup'),
	url(r'^signout/$', 'accounts.views.signout'),
)
