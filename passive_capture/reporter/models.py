from django.db import models

# Create your models here.
class Forecasts(models.Model):
  species = models.CharField(max_length=20)
  dam = models.CharField(max_length=20)
