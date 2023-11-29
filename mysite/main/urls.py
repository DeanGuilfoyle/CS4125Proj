from django.urls import path
from . import views
from .views import CarListView
from .views import manage_cars

urlpatterns = [
    #path("", views.index, name="index"),
    #path("create/", views.create, name="create"),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('car-list/', CarListView.as_view(), name='car-list'),
    path('manage-cars/', manage_cars, name='manage-cars'),
    path('send-promotion/', views.send_promotion_email, name='send_promotion'),

]
