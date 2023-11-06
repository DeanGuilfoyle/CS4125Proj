from urllib.parse import urlencode
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import CarFilterForm
from .models import Car, Booking

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

class CarListView(ListView):
    model = Car
    template_name = 'main/car_list.html'  # Create this template next
    context_object_name = 'cars'
    object_list = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarFilterForm(self.request.GET)
        return context
    
    def get(self, request, *args, **kwargs):
        #get filters from the URL
        car_make = request.GET.get('car_make')
        car_year = request.GET.get('car_year')
        car_colour = request.GET.get('car_colour')
        max_price = request.GET.get('max_price')

        #Start with a list of all cars
        cars = Car.objects.all()

        #Apply filters to our cars list
        if car_make:
            cars = cars.filter(make=car_make)
        if car_year:
            cars = cars.filter(year=car_year)
        if car_colour:
            cars = cars.filter(colour=car_colour)
        if max_price is not None:
            cars = cars.filter(price_per_day__lte=max_price)
        
        #self.object_list = cars

        #place our now filtered list into our context object to be sent to the template
        custom_context = {
            'filtered_cars': cars,
        }

        context = self.get_context_data()
        context.update(custom_context)

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = CarFilterForm(request.POST)
        cars = Car.objects.all()  # Start with all cars
        if form.is_valid():
            
            #take filter results which the user has given
            car_make = form.cleaned_data.get('car_make')
            car_year = form.cleaned_data.get('car_year')
            car_colour = form.cleaned_data.get('car_colour')
            max_price = form.cleaned_data.get('max_price')

            #Start with a list of all cars
            cars = Car.objects.all()

            #Apply filters to our cars
            if car_make:
                cars = cars.filter(make=car_make)
            if car_year:
                cars = cars.filter(year=car_year)
            if car_colour:
                cars = cars.filter(colour=car_colour)
            if max_price is not None:
                cars = cars.filter(price_per_day__lte=max_price)

            #Store the selected filters in our url
            url_params = {}
            if car_make:
                url_params['car_make'] = car_make
            if car_year:
                url_params['car_year'] = car_year
            if car_colour:
                url_params['car_colour'] = car_colour
            if max_price is not None:
                url_params['max_price'] = max_price

            # Redirect to the URL with the updated query parameters
            return redirect(f'{self.request.path_info}?{urlencode(url_params)}')

        #self.object_list = cars

        custom_context = {
            'filtered_cars': cars,
        }

        context = self.get_context_data()
        context.update(custom_context)

        return render(request, self.template_name, context)

class BookCars(ListView):
    model = Car 
    template_name = 'main/book_car.html'
    context_object_name = 'cars'
    object_list = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarFilterForm(self.request.GET)
        return context
    
    def get(self, request, *args, **kwargs):
        #get filters from the URL
        car_make = request.GET.get('car_make')
        car_year = request.GET.get('car_year')
        car_colour = request.GET.get('car_colour')
        max_price = request.GET.get('max_price')

        #Start with a list of all cars
        cars = Car.objects.all()

        #Apply filters to our cars list
        if car_make:
            cars = cars.filter(make=car_make)
        if car_year:
            cars = cars.filter(year=car_year)
        if car_colour:
            cars = cars.filter(colour=car_colour)
        if max_price is not None:
            cars = cars.filter(price_per_day__lte=max_price)
        
        #self.object_list = cars

        #place our now filtered list into our context object to be sent to the template
        custom_context = {
            'filtered_cars': cars,
        }

        context = self.get_context_data()
        context.update(custom_context)

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = CarFilterForm(request.POST)
        cars = Car.objects.all()  # Start with all cars
        if form.is_valid():
            
            #take filter results which the user has given
            car_make = form.cleaned_data.get('car_make')
            car_year = form.cleaned_data.get('car_year')
            car_colour = form.cleaned_data.get('car_colour')
            max_price = form.cleaned_data.get('max_price')

            #Start with a list of all cars
            cars = Car.objects.all()

            #Apply filters to our cars
            if car_make:
                cars = cars.filter(make=car_make)
            if car_year:
                cars = cars.filter(year=car_year)
            if car_colour:
                cars = cars.filter(colour=car_colour)
            if max_price is not None:
                cars = cars.filter(price_per_day__lte=max_price)

            #Store the selected filters in our url
            url_params = {}
            if car_make:
                url_params['car_make'] = car_make
            if car_year:
                url_params['car_year'] = car_year
            if car_colour:
                url_params['car_colour'] = car_colour
            if max_price is not None:
                url_params['max_price'] = max_price

            # Redirect to the URL with the updated query parameters
            return redirect(f'{self.request.path_info}?{urlencode(url_params)}')

        #self.object_list = cars

        custom_context = {
            'filtered_cars': cars,
        }

        context = self.get_context_data()
        context.update(custom_context)

        return render(request, self.template_name, context)


 






