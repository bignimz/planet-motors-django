from django.shortcuts import get_object_or_404, render
from cars.models import Car
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def cars(request):
    cars = Car.objects.all().order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    context = {
        'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    # car_features = Car.objects.filter('features', pk=id)

    context = {
        'single_car': single_car,
        # 'car_features': car_features,
    }
    return render(request, 'cars/car_detail.html', context)

def search(request):
    cars = Car.objects.order_by('-created_date')
    context = {'cars': cars}
    return render(request, 'cars/search.html', context)