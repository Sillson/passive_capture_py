from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Forecasts, Dam, Species

def index(request):
    dams = Dam.objects.all().values()

    species = Species.objects.all().values()
    
    return render(request, 'index.html', context={'dams':dams, 'species':species})

def view_dam(request, id):
    try:
        dam = Dam.objects.get(id=id)
    except Dam.DoesNotExist:
        raise Http404("Dam does not exist")
 
    return render(request, 'dam.html', context={'dam': dam})

def view_species(request, id):
    try:
        species = Species.objects.get(id=id)
    except Species.DoesNotExist:
        raise Http404("Species does not exist")
 
    return render(request, 'species.html', context={'species': species})

def view_forecasts(request, id):
    try:
        forecast = Forecasts.objects.get(id=id)
    except Forecasts.DoesNotExist:
        raise Http404("Forecast does not exist")
 
    return render(request, 'forecast.html', context={'forecast': forecast})