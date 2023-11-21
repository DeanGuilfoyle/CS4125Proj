from django.urls import path
from . import views
from .views import CarListView
from .views import BookCars

urlpatterns = [
    #path("", views.redirect, name="redirect"),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('car-list/', CarListView.as_view(), name='car-list'),
    path('book-car/', BookCars.as_view(), name='book-car'),
    path("home", views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('send-promotion/', views.send_promotion_email, name='send_promotion'),
]