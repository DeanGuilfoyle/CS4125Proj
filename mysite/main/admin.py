from django import forms
from django.contrib import admin
from .models import Car, Sedan, Coupe

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price_per_day', 'is_available')

    form = forms.ModelForm

    def get_bookings(self, obj): # creating method 
        bookings = Booking.objects.filter(car=obj) # filters through booking + includes only those related to specified car obj
        return ", ".join([f"{booking.user.username} ({booking.booking_date})" for booking in bookings]) # creating a formatted list 


admin.site.register(Sedan)
admin.site.register(Coupe)