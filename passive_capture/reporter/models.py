from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.utils import timezone

class Dam(models.Model):
  name = models.CharField(max_length = 20)
  abbr = models.CharField(max_length = 5)
  location = models.PointField(srid=4326)
  # deprecated
  objects = GeoManager()

  def __str__(self):
    return self.abbr

class Species(models.Model):
  name = models.CharField(max_length = 25)
  reference_name = models.CharField(max_length = 25)

  class Meta:
    verbose_name_plural = "Species"

  def __str__(self):
    return self.name

  def hux(self, blarg='fins'):
    return f"{self.name} is a really neat fish with {blarg}"

class Forecasts(models.Model):
  species = models.ForeignKey(Species, on_delete=False)
  dam = models.ForeignKey(Dam, on_delete=False)
  forecast_range = models.DateField(default=timezone.now, blank=True)
  graph = models.FileField(blank=True)
  forecast_csv = models.FileField(blank=True)

  def __str__(self):
    return self.dam.abbr + '_' + self.species.reference_name

  class Meta:
    verbose_name_plural = "Forecasts"

  def graph_path(self):
    return f"../static/images/forecasts/{self.dam.abbr}_{self.species.reference_name}_forecast.png"

  def forecast_csv_path(self):
    return f"../static/csv/forecasts/{self.dam.abbr}_{self.species.reference_name}_forecast.csv"




