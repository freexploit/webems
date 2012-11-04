from emulations.models import ExtendedFlatPage
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        e = ExtendedFlatPage(url="/1/", title="one", updated_by=1, created_by=1, content="<html><head><title>one</title></head><body>this is page one</body></html>", original_html="<html><head><title>one</title></head><body>this is page one</body></html>", page_url="http://www.wisc.edu/")
        e.save()
        e.site = [1]
        e.save()
        e = ExtendedFlatPage(url="/2/", title="two", updated_by=1, created_by=1, content="<html><head><title>two</title></head><body>this is page two</body></html>", original_html="<html><head><title>two</title></head><body>this is page two</body></html>", page_url="http://www.economist.com/")
        e.save()
        e.site = [1]
        e.save()