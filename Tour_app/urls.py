from django.urls import path, include
from .views import *
urlpatterns = [

    path('', index,name="Home"),
    path('tour_packages/', tour_packages,name="tour_packages"),
    path('tour_package/<int:id>', package_details,name="package_details"),
    path('contact/', contact,name="contact"),
    path('about/', about,name="about"),
    path('search/', search,name="search"),
    path('submit_inquiry/', submit_inquiry,name="submit_inquiry"),
]