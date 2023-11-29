from django.db import models
from django.contrib.auth.models import User
from . import pricing_states
from .decorators import PricingDecorator, InsuranceDecorator


# Create your models here.
class Car(models.Model):
    COLOUR_CHOICES = (
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Brown', 'Brown'),
    ('Gray', 'Gray'),
    ('Green', 'Green'),
    ('LightBlue', 'LightBlue'),
    ('Navy', 'Navy'),
    ('Red', 'Red'),
    ('Silver', 'Silver'),
    ('White', 'White'),
    )

    YEAR_CHOICES = (
        (2023, '2023'),
        (2022, '2022'),
        (2021, '2021'),
        (2020, '2020'),
        (2019, '2019'),
        (2018, '2018'),
        (2017, '2017'),
        (2016, '2016'),
        (2015, '2015'),
    )

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colour = models.CharField(max_length=20, choices=COLOUR_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    pricing_state = models.CharField(max_length=20, default='RegularPricingState') 

    def calculate_rental_price(self, car_price):
        # Instantiate the current pricing state and calculate the price
        current_state = getattr(pricing_states, self.pricing_state)()
        rental_price = current_state.calculate_price(car_price)
        decorated_car = InsuranceDecorator(self)
        return decorated_car.calculate_price(rental_price)

# sedan inherits from car model and has additional field
class Sedan(Car):
    trunk_capacity = models.IntegerField()
    pass

# coupe inherits from car model and has additional field
class Coupe(Car):
    has_panoramic_roof = models.BooleanField(default=False)
    pass