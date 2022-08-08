from ast import keyword
from pydoc import describe
from django.shortcuts import get_object_or_404, render
from cars.models import Car
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def cars(request):
    cars = Car.objects.all().order_by('-created_date')
    paginator = Paginator(cars, 6)
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
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    condition_search = Car.objects.values_list('condition', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)


    context = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'condition_search': condition_search,
        }
    return render(request, 'cars/search.html', context)