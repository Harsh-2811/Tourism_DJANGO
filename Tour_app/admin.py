from django.contrib import admin
from django.shortcuts import render
from django.utils.html import format_html

from .models import *


class CountryAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="80" style="border-radius:50px">'.format(object.image.url))

    list_display = ('id','name','description','thumbnail')
    list_display_links = ('id','name')

admin.site.register(Countries,CountryAdmin)

class PlaceAdmin(admin.TabularInline):
    model = Tour_place_hotel
    extra = 0

class Tour_ItineraryAdmin(admin.TabularInline):
    model = Tour_Itinerary
    extra = 0

class PlaceModelAdmin(admin.ModelAdmin):
    list_display = ('id','package','title','details',)
    list_display_links   = ('id','package','title',)

admin.site.register(Tour_Itinerary,PlaceModelAdmin)
class PackageAdmin(admin.ModelAdmin):
    inlines = [PlaceAdmin,Tour_ItineraryAdmin ]

    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:50px">'.format(object.image.url))

    def places(self,object):
        place_list_dummy= object.get_places()
        place_list = []
        for val in place_list_dummy:
            place_list.append(val)
        return place_list

    list_display = ('id','title','departure','places','no_of_days','destination','country','cost_per_person','is_available','is_full','max_capacity','thumbnail')
    list_display_links = ('id','title')
    list_editable = ('cost_per_person','is_available')

admin.site.register(Tour_package,PackageAdmin)

class Place_hotel_Admin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="80" height="50px" style="border-radius:50px">'.format(object.place_image.url))
    list_display = ['id','hotel','place','package','thumbnail']
    list_display_links = ['id']

admin.site.register(Tour_place_hotel,Place_hotel_Admin)

class HotelAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30"  style="border-radius:50px">'.format(object.image.url))
    list_display = ['id', 'name', 'location', 'country','total_rooms','thumbnail']
    list_display_links = ['id','name']
admin.site.register(Hotel,HotelAdmin)

class RoomAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30" style="border-radius:50px">'.format(object.image.url))
    list_display = ['id', 'type', 'hotel', 'price','bed_details','capacity','thumbnail']
    list_display_links = ['id','type']

admin.site.register(Room,RoomAdmin)


class ContactAdmin(admin.ModelAdmin):

    list_display = ['id','name','email','subject','message']
    list_display_links = ['id','name']

admin.site.register(ContactU,ContactAdmin)

class Inquiry_admin(admin.ModelAdmin):


    list_display = ['id','date','interested_date','package','name','phone','email']
    list_display_links = ['id','package']

admin.site.register(Tour_Inquiry,Inquiry_admin)

