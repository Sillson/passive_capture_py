from django.contrib import admin
from django.contrib.gis import admin as geo_model_admin
from .models import Forecasts
from .models import Dam
from .models import Species

# Forecast Model
class ForecastsAdmin(admin.ModelAdmin):
  list_display = ('dam', 'species')

admin.site.register(Forecasts, ForecastsAdmin)

# Species Model
class SpeciesAdmin(admin.ModelAdmin):
  list_display = ('name', 'reference_name')

admin.site.register(Species, SpeciesAdmin)

# Dam Model - requires GeoAdmin privelages
class DamAdmin(geo_model_admin.OSMGeoAdmin):
  list_display = ('name', 'abbr', 'location')

geo_model_admin.site.register(Dam, DamAdmin)

