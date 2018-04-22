from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.utils import timezone
import folium
import os.path

# from .forecast_generator import add_stf

class Dam(models.Model):
  name = models.CharField(max_length = 20)
  abbr = models.CharField(max_length = 5)
  location = models.PointField(srid=4326)
  # deprecated
  objects = GeoManager()

  def __str__(self):
    return self.abbr

  def create_map(self):
    coords = self.location.coords
    coords = [coords[1],coords[0]]
    m = folium.Map(
                    location=coords,
                    zoom_start=11
                )
    folium.CircleMarker(
                        location=coords,
                        radius=50,
                        popup=self.name,
                        color='#3186cc',
                        fill=True,
                        fill_color='#3186cc'
                        ).add_to(m)
    m.save(f"reporter/static/maps/{self.abbr}.html")

  def save(self, *args, **kwargs):
    created = self.pk is None
    super(Dam, self).save(*args, **kwargs)
    if os.path.isfile(f"reporter/static/maps/{self.abbr}.html"):
      os.remove(f"reporter/static/maps/{self.abbr}.html")
      self.create_map()
    else:
      self.create_map()

  def map_path(self):
    return f"{self.abbr}.html"

class Species(models.Model):
  name = models.CharField(max_length = 25)
  reference_name = models.CharField(max_length = 25)

  class Meta:
    verbose_name_plural = "Species"

  def __str__(self):
    return self.name

class Forecasts(models.Model):
  species = models.ForeignKey(Species, on_delete=False)
  dam = models.ForeignKey(Dam, on_delete=False)
  forecast_range = models.DateField(default=timezone.now, blank=True)
  graph = models.FileField(upload_to=f"reporter/static/images/forecasts/",blank=True)
  forecast_csv = models.FileField(upload_to=f"reporter/static/csv/forecasts/",blank=True)

  def __str__(self):
    return self.dam.abbr + '_' + self.species.reference_name

  class Meta:
    verbose_name_plural = "Forecasts"

  def graph_path(self):
    return f"{self.dam.abbr}_{self.species.reference_name}_forecast.png"

  def forecast_csv_path(self):
    return f"{self.dam.abbr}_{self.species.reference_name}_forecast.csv"




