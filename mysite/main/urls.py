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
]