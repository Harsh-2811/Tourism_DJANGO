from django.urls import path, include
from .views import *
urlpatterns = [

path('logout/',logoutProcess,name="logoutProcess"),
path('login/',loginProcess,name="loginProcess"),
path('register/',registerProcess,name="registerProcess"),

]