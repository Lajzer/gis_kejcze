from django.shortcuts import render
from .models import Package, GeocachingUser

# Create your views here.
def index(request):

    context = {}
    return render(request, 'geocaching/index.html', context)
