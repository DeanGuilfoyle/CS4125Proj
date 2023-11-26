from django.db import models
from django.contrib.auth.models import User


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

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_days = models.PositiveIntegerField(default=1)



