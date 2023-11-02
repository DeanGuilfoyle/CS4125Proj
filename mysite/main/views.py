from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Car

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

class CarListView(ListView):
    model = Car
    template_name = 'main/car_list.html'  # Create this template next
    context_object_name = 'cars'
