"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from project.views import home

urlpatterns = [
    # Define the URL pattern for the home page, which maps to the 'home' view.
    path('', home, name='home'),
    
    # URL pattern for the admin site.
    path('admin/', admin.site.urls),
    
    # URL pattern for including the 'playground' app's URLs.
    path('playground/', include('playground.urls')),
    
    # Add an alternative URL pattern for '/home' that also maps to the 'home' view.
    path('home/', home),  # This allows you to access the home page at '/home'.
]
