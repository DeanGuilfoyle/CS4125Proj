from urllib.parse import urlencode
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import CarFilterForm
from .models import Car, Booking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from observer.subject import PromotionService
from django.http import HttpResponseRedirect
from django.urls import reverse
from observer.observers import EmailAlertObserver


# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})


# only staff users can use it
@staff_member_required
def send_promotion_email(request):
    if request.method == 'POST':
        # Gets all users who are not staff and have an email address
        users = User.objects.filter(is_staff=False).exclude(email='')

        # Creates a PromotionService instance and attaches observers for each users email
        promotion_service = PromotionService()
        for user in users:  
            observer = EmailAlertObserver(user.email)
            promotion_service.attach(observer)

        # sends the message to observers
        promotion_service.notify('Promotion on from the 6th to the 16th of November! 20% off selected models!')

        # Redirect back to the homepage with a success message
        return HttpResponseRedirect(reverse('home'))
    

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

        update_pricing()
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
        
        # Calculate prices for each car
        for car in cars:
            car.rental_price = car.calculate_rental_price(car.price_per_day) 
            car.save()

        #place our now filtered list into our context object to be sent to the template
        custom_context = {
            'filtered_cars': cars,
            'cars': cars,
        }

        context = self.get_context_data()
        context.update(custom_context)

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = CarFilterForm(request.POST)
        update_pricing()
        cars = Car.objects.all()  # Start with all cars
        if form.is_valid():
            
            #take filter results which the user has given
            car_make = form.cleaned_data.get('car_make')
            car_year = form.cleaned_data.get('car_year')
            car_colour = form.cleaned_data.get('car_colour')
            max_price = form.cleaned_data.get('max_price')

            #Start with a list of all cars
            #cars = Car.objects.all()

            """#Apply filters to our cars
            if car_make:
                cars = cars.filter(make=car_make)
            if car_year:
                cars = cars.filter(year=car_year)
            if car_colour:
                cars = cars.filter(colour=car_colour)
            if max_price is not None:
                cars = cars.filter(price_per_day__lte=max_price)"""

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

        
        # Calculate prices for each car
        for car in cars:
            car.rental_price = car.calculate_rental_price(car.price_per_day) 
            car.save()

        custom_context = {
            'filtered_cars': cars,
            'cars': cars,
        }

        context = self.get_context_data()
        context.update(custom_context)

        return render(request, self.template_name, context)

@login_required
def book_car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':
        booking_days = int(request.POST.get('booking_days', 1))
        booking = Booking.objects.create(user=request.user, car=car, booking_days=booking_days)

        # Making car unavailable after being booked
        car.is_available = False
        car.save()

        return redirect('manage-booking', booking_id=booking.id)

    return render(request, 'main/book_car_detail.html', {'car': car})

@login_required
def manage_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    # Calculating price based on total days booked
    update_pricing()
    price_per_day = booking.car.calculate_rental_price(booking.car.price_per_day)
    total_price = booking.car.calculate_rental_price(booking.car.price_per_day) * booking.booking_days 

    return render(request, 'main/manage_booking.html', {'booking': booking, 'total_price': total_price, "price_per_day": price_per_day})

def update_pricing():
    cars = Car.objects.all()

    current_date = datetime.date.today()

    # Update pricing state for each car based on conditions
    for car in cars:

        # Set pricing state based on conditions
        if current_date.weekday() in [5, 6]:  # 5 and 6 correspond to Saturday and Sunday
            car.pricing_state = 'WeekendPricingState'
        #elif current_date == event:
            #car.pricing_state = 'PromotionPricingState'
        else:
            car.pricing_state = 'RegularPricingState'

        car.save()

 






