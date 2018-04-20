from django.contrib import admin
from django.contrib.gis import admin as geo_model_admin
from leaflet.admin import LeafletGeoAdmin
from .models import Forecasts, Dam, Species

# Forecast Model
class ForecastsAdmin(admin.ModelAdmin):
  list_display = ('dam', 'species', 'forecast_range')

admin.site.register(Forecasts, ForecastsAdmin)

# Species Model
class SpeciesAdmin(admin.ModelAdmin):
  list_display = ('name', 'reference_name')

admin.site.register(Species, SpeciesAdmin)

# Dam Model - requires GeoAdmin privelages
class DamAdmin(LeafletGeoAdmin):
  list_display = ('name', 'abbr', 'location')

admin.site.register(Dam, DamAdmin)

