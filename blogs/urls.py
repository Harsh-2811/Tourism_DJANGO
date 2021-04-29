from django.urls import path, include
from .views import *
urlpatterns = [

    path('', blogs,name="blogs"),
    path('<str:slug>/', single_blog,name="blog_slug"),

]