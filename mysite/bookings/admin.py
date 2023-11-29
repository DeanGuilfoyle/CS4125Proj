from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'created_at')
    list_filter = ('user', 'car', 'created_at')
    search_fields = ('user__username', 'car__make', 'car__model')