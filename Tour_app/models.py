from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Min, Count, Sum
from django.dispatch import receiver
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField

from django.utils.timezone import now
# Create your models here.
from users.models import CustomUser


class Countries(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="images")
    description = models.TextField()


    def __str__(self):
        return self.name

    def get_tour_count(self):
        return Tour_package.objects.filter(country__iexact=self.name).count()

class Tour_package(models.Model):
    main_place   = [
        ('Mountain','Mountain'),
        ('Beach','Beach'),
        ('City','City')
    ]

    Month_list = (
        ("Whole Year","Whole Year"),
        ("Jan","Jan"),
        ("Fab","Fab"),
        ("Mar","Mar"),
        ("April","April"),
        ("May","May"),
        ("Jun","Jun"),
        ("July","July"),
        ("Aug","Aug"),
        ("Sept","Sept"),
        ("Oct","Oct"),
        ("Nov","Nov"),
        ("Dec","Dec"),

    )
    id = models.AutoField(primary_key = True)
    Tour_ID = models.CharField(max_length=100,default=" ")
    title = models.CharField(max_length=100)
    no_of_days = models.IntegerField()
    image = models.ImageField(upload_to='images')
    Nearest_nature_place = models.CharField(choices=main_place,max_length=100)
    details = models.TextField()
    destination = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    cost_per_person = models.DecimalField(max_digits=10,decimal_places=0)
    departure =  MultiSelectField(choices=Month_list,default=" ")
    is_available = models.BooleanField(default=True)
    is_full = models.BooleanField(default=False)
    max_capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_places(self):
        tour_places_result = Tour_place_hotel.objects.filter(package=self).values_list('place',flat=True)
        return tour_places_result

    def get_tour_places(self):
        places = Tour_place_hotel.objects.filter(package=self)
        return places

    def split_departure(self):
        return self.departure.split(',')

class Tour_Itinerary(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Tour_package,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default="")
    day_no = models.IntegerField(default=1)
    details = RichTextField()

    def __str__(self):
        return str(self.id)

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')
    rating = models.IntegerField(default=1)
    no_of_rating = models.IntegerField(default=10)
    checkin_time = models.TimeField(default=timezone.now)
    checkout_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def rooms_types(self):
        rooms = Room.objects.filter(hotel=self)
        room_list = []
        for room in rooms:
            room_list.append(room)
        return room_list


    def get_low_cost_room(self):

        price = Room.objects.filter(hotel=self).aggregate(Min('price'))
        if price['price__min']:
            return price['price__min']
        else:
            return 0

class Room(models.Model):

    Amenities_List = [
        ('Air Conditioning','Air Conditioning'),
        ('Free Wi-Fi','Free Wi-Fi'),
        ('Restaurant/Coffee Shop','Restaurant/Coffee Shop'),
        ('CCTV','CCTV'),
        ('Room Service','Room Service'),
        ('Swimming Pool','Swimming Pool'),
    ]

    id = models.AutoField(primary_key=True)
    room_no = models.CharField(max_length=500,default="")
    type = models.CharField(max_length=200)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    price= models.DecimalField(max_digits=10,decimal_places=2)
    bed_details = models.CharField(max_length=30)
    capacity = models.CharField(max_length=30)
    Amenities = MultiSelectField(choices=Amenities_List,default=" ")

    def __str__(self):
        return self.type

class Tour_place_hotel(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Tour_package, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    place = models.CharField(default=" ",max_length=100)
    place_image = models.ImageField(upload_to="image",default="/static/images/destination-8.jpg")
    def __str__(self):
        return "Place is {} and Hotel is {}".format(self.place,self.hotel.name)


class ContactU(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return "{} asked or Informed about {}".format(self.name,self.subject)

class Tour_Inquiry(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    interested_date= models.DateField()
    package = models.ForeignKey(Tour_package, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    people = models.IntegerField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return "{} has sent inquiry about {}".format(self.name,self.package)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    person = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING)
    no_of_rooms = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=10,decimal_places=2)
    check_in  = models.DateField()
    check_out  = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} has booked {} rooms of type {}".format(self.person,self.no_of_rooms,self.room)





