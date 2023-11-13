from .models import Car
from django.contrib.auth.models import User

class CarFactory:
    @staticmethod # allows calling on the class without needing an instance of it
    def create_car(make, model, colour, year, price_per_day, is_available=True):
        return Car.objects.create(
            make=make,
            model=model,
            colour=colour,
            year=year,
            price_per_day=price_per_day,
            is_available=is_available
        )
    
# Can create instances of the car model with specific attributes and then insert that into the database
# Changes to car instances only need to be made in the factory class, rather than in all the other classes it is in


# python manage.py shell

#from main.factories import CarFactory

#car_instance = CarFactory.create_car(
#    make='Nissan',
 #   model='Altima',
 #   colour='Green',
 #   year=2020,
 #   price_per_day=60.00,
 #   is_available=True
#)
