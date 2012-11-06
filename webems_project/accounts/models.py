from django.contrib.auth.models import User
from django.db import models
from emulations.models import ExtendedFlatPage

class MyEmulations(models.Model):
    user = models.ForeignKey(User)
    emulations = models.ManyToManyField(ExtendedFlatPage)