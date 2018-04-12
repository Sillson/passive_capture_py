from django.contrib import admin
from .models import Forecasts
from .models import Dam
from .models import Species

# Register your models here.
class ForecastsAdmin(admin.ModelAdmin):
  list_display = ('dam', 'species')

admin.site.register(Forecasts, ForecastsAdmin)

class SpeciesAdmin(admin.ModelAdmin):
  list_display = ('name', 'reference_name')

admin.site.register(Species, SpeciesAdmin)

class DamAdmin(admin.ModelAdmin):
  list_display = ('name', 'abbr', 'location')

admin.site.register(Dam, DamAdmin)

