from django.urls import path
from . import views
from .views import CarListView
from .views import BookCars

urlpatterns = [
    #path("", views.index, name="index"),
    #path("create/", views.create, name="create"),
    path("", views.home, name="home"),
    path('car-list/', CarListView.as_view(), name='car-list'),
    path('book-car/', BookCars.as_view(), name='book-car'),
    path('book-car/<int:car_id>/', views.book_car_detail, name='book-car-detail'),
    path('manage-booking/<int:booking_id>/', views.manage_booking, name='manage-booking'),
]