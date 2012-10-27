from django.contrib.auth.models import User
import datetime
from django.db import models
from django.contrib.flatpages.models import FlatPage

class ExtendedFlatPage(FlatPage):
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(default=datetime.datetime.now)
    page_url = models.TextField()
    original_html = models.TextField()

    class Meta:
        # sort by "the date" in descending order unless
        # overridden in the query with order_by()
        ordering = ['-created']

class MyEmulations(models.Model):
	user = models.ForeignKey(User)
	emulation = models.ForeignKey(ExtendedFlatPage)

class Rewrites(models.Model):
	METHODS = (
        (u'S', u'normal_string'),
        (u'PR', u'python_rejex'),
    )
	find = models.TextField()
	replace = models.TextField()
	method = models.CharField(max_length=2, choices=METHODS, default='S')