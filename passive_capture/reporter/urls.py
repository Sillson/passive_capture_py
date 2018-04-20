from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('dams/<int:id>/', views.view_dam),
  path('species/<int:id>/', views.view_species),
  path('forecasts', views.forecasts_index),
  path('forecasts/<int:id>/', views.view_forecasts),
  path('about', views.about)
]