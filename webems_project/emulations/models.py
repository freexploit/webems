from django.contrib.auth.models import User
import datetime
from django.db import models
from django.contrib.flatpages.models import FlatPage

class ExtendedFlatPage(FlatPage):
    created = models.DateTimeField(default=datetime.datetime.now)
    created_by = models.IntegerField()
    updated = models.DateTimeField(default=datetime.datetime.now)
    updated_by = models.IntegerField()
    page_url = models.TextField()
    original_html = models.TextField()

    @property
    def creator(self):
        return User.objects.get(id=self.created_by) 

    @property
    def updator(self):
        return User.objects.get(id=self.updated_by)

    class Meta:
        # sort by "the date" in descending order unless
        # overridden in the query with order_by()
        ordering = ['-created']

def save(self, *args, **kwargs):
    print 'ya', self.args
    #track the creator/last editor via an optional kwarg
    active_user = self.kwargs.get('user')
    if active_user:
       self.updated_by = active_user
    if active_user and not self.created_by:
       self.created_by = active_user
    return super(AuditBase, self).save(*args, **kwargs)

class Rewrites(models.Model):
	METHODS = (
        (u'S', u'normal_string'),
        (u'PR', u'python_rejex'),
    )
	find = models.TextField()
	replace = models.TextField()
	method = models.CharField(max_length=2, choices=METHODS, default='S')