from operator import is_
from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.

def index(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_date')
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }

    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')