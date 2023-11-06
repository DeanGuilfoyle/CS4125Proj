from django.shortcuts import render, redirect
from django.views.generic import ListView
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

class BookCars(ListView):
    model = Car 
    template_name = 'main/book_car.html'
    context_object_name = 'cars'

 






