
from django.contrib import admin
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("main.urls")),
    path('', include("main.urls")),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('bookings/', include('bookings.urls')),
]
