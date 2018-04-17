from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

class Dam(models.Model):
  name = models.CharField(max_length = 20)
  abbr = models.CharField(max_length = 5)
  location = models.PointField(srid=4326)
  # deprecated
  objects = GeoManager()

class Species(models.Model):
  name = models.CharField(max_length = 25)
  reference_name = models.CharField(max_length = 25)

  class Meta:
    verbose_name_plural = "Species"

class Forecasts(models.Model):
  species = models.ForeignKey(Species, on_delete=False)
  dam = models.ForeignKey(Dam, on_delete=False)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name_plural = "Forecasts"



