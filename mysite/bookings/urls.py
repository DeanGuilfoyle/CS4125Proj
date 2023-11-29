from django.urls import path
from . import views

urlpatterns = [
    path('bookings/book-car/<int:car_id>/', views.book_car, name='book-car'),  
    path('bookings/cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel-booking'),
    path('view-bookings/', views.view_bookings, name='view-bookings'), 
    path('view-all-bookings/', views.view_all_bookings, name='view-all-bookings'),
    path('booking-success/', views.booking_success, name='booking-success'),
]

