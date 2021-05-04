from datetime import datetime,timedelta

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
from blogs.models import Blog
from .Booking_check.Check_Avaiablity import check_availablity
# Create your views here.
def index(request):

    blogs = Blog.objects.filter(status="1").order_by('-date')[:3]
    countries = Countries.objects.all().order_by('id')
    packages = Tour_package.objects.filter(is_available=True).order_by('id')
    days= Tour_package.objects.values_list('no_of_days',flat=True)
    cost= Tour_package.objects.values_list('cost_per_person',flat=True)
    start_date = datetime.today().date()
    end_date = datetime.today().date() + timedelta(days=1)
    return render(request,"index.html",{'countries':countries,'packages':packages,'blogs':blogs,'days':days,'costs':cost,'todays_date':start_date,'tommorow_date':end_date})

def search(request):
    packages = Tour_package.objects.filter(is_available=True).order_by('id')
    print(request.GET)
    days = Tour_package.objects.values_list('no_of_days', flat=True)
    cost = Tour_package.objects.values_list('cost_per_person', flat=True)
    if 'destination' in request.GET:
        keyword = request.GET['destination']
        if keyword:
            packages= packages.filter(destination__icontains=request.GET['destination'])
        print('destination')

    if 'country' in request.GET:
        keyword = request.GET['country']
        if keyword:
            packages = packages.filter(country__iexact=request.GET['country'])
        print('country')

    if 'days' in request.GET:
        keyword = request.GET['days']
        if keyword:
            packages = packages.filter(no_of_days=int(request.GET['days']))
        print(packages)

    if 'price' in request.GET:
        keyword = request.GET['price']

        if float(keyword) > 0:
            packages = packages.filter(cost_per_person__lte=keyword)

    paginator = Paginator(packages, 9)
    page = request.GET.get('page')
    paged_packages = paginator.get_page(page)

    return render(request, "destination.html", {'packages': paged_packages,'days':days,'costs':cost})



def tour_packages(request):
    packages = None
    country =  False
    if request.GET.get('country',False):
        country_name = request.GET['country']
        packages = Tour_package.objects.filter(is_available=True,country__iexact=country_name).order_by('id')
        paginator = Paginator(packages, 9)
        page = request.GET.get('page')
        paged_packages = paginator.get_page(page)
        country = Countries.objects.get(name__iexact=country_name)
    else:
        packages = Tour_package.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(packages, 9)
        page = request.GET.get('page')
        paged_packages = paginator.get_page(page)

    days = Tour_package.objects.values_list('no_of_days', flat=True)
    cost = Tour_package.objects.values_list('cost_per_person', flat=True)
    return render(request, "destination.html", {'packages': paged_packages,'country':country,'days':days,'costs':cost})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contactmessage = ContactU(name=name,email=email,subject=subject,message=message)
        contactmessage.save()

        messages.success(request,'Your Inquiry Submitted Successfully')

    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def package_details(request,id):

    package = get_object_or_404(Tour_package,pk=id)
    itinerary = Tour_Itinerary.objects.filter(package=package)
    today_date = datetime.today().date()
    print(today_date)
    return render(request,"Package_detail.html",{'package':package,'itineraries':itinerary,'today_date':today_date})

def submit_inquiry(request):

    if request.method == "POST":
        tour_id = request.POST['tour_id']
        Intrastate_date  = request.POST['Intrastate_date']

        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        address = request.POST['address']
        name = request.POST['name']
        people = request.POST['no_of_person']

        package = get_object_or_404(Tour_package,pk=tour_id)
        inquiry = Tour_Inquiry(date=datetime.today().date(),interested_date=Intrastate_date,package=package,
                               email=email,phone=phone,city=city,state=state,country=country,address=address,name=name,
                               people=people)
        inquiry.save()
        messages.success(request,"Your Inquiry has been sent. We will Send Details on your email and phone")
        return redirect("/tour_package/"+tour_id)


def hotels(request):


    Start_date = datetime.today().date()
    End_date = datetime.today().date()+timedelta(days=1)
    rooms  = Room.objects.order_by('-hotel__rating','id')
    hotels = []

    if 'apply_filter' in request.GET:

        if 'check_in_date' in request.GET and 'check_out_date' in request.GET:
            Start_date = request.GET['check_in_date']
            End_date = request.GET['check_out_date']

            print(Start_date,End_date)

        if 'destination' in request.GET:
            keyword = request.GET['destination']
            rooms = rooms.filter(hotel__location__icontains=keyword)
            print(rooms)


        if 'price' in request.GET:
            keyword = request.GET['price']
            if float(keyword) > 0:
                rooms = rooms.filter(price__lte=keyword)

        check_in = datetime.strptime(Start_date, "%b/%d/%Y")
        check_out = datetime.strptime(End_date, "%b/%d/%Y")
        Start_date = check_in
        End_date = check_out
        for room in rooms:
            if check_availablity(room, datetime.date(check_in), datetime.date(check_out)):
                if room.hotel not in hotels:
                    hotels.append(room.hotel)
    else:
        for room in rooms:
            if check_availablity(room, Start_date, End_date):
                if room.hotel not in hotels:
                    hotels.append(room.hotel)

    paginator = Paginator(hotels, 6)
    page = request.GET.get('page')
    pagged_hotels = paginator.get_page(page)

    return render(request,'hotel.html',{'hotels_data':pagged_hotels,'todays_date':Start_date,'tommorow_date':End_date})

def hotel_detail(request,id):
    hotel = get_object_or_404(Hotel, pk=id)
    hotel_rooms = Room.objects.filter(hotel=hotel)
    start_date = datetime.today().date()
    end_date = datetime.today().date() + timedelta(days=1)
    rooms = []

    if 'check_in_date' in request.GET and 'check_out_date' in request.GET:
        start_date = request.GET['check_in_date']
        end_date = request.GET['check_out_date']

        if start_date:
                check_in = datetime.strptime(start_date,"%b/%d/%Y")
                check_out =datetime.strptime(end_date,"%b/%d/%Y")
                for room in hotel_rooms:
                    if check_availablity(room, datetime.date(check_in) ,datetime.date(check_out) ):
                        rooms.append(room)


    else:
        for room in hotel_rooms:
            if check_availablity(room,datetime.today().date(),datetime.today().date()+timedelta(days=1)):
                rooms.append(room)

    return render(request,'Hotel_Detail.html',{'hotel':hotel,'rooms':rooms,'todays_date':start_date,'tommorow_date':end_date})

def book_room(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            room_id = request.POST['room_id']
            room = get_object_or_404(Room,id=room_id)
            hotel = room.hotel
            person = request.user
            no_of_rooms = request.POST['no_of_rooms']
            amount_paid = float(no_of_rooms)*float(room.price)
            check_in = request.POST['hidden_checkin']
            check_out = request.POST['hidden_checkout']
            check_in = datetime.strptime(check_in, "%b/%d/%Y")
            check_out = datetime.strptime(check_out, "%b/%d/%Y")
            booking = Booking(room=room,hotel=hotel,person=person,no_of_rooms=no_of_rooms,amount_paid=amount_paid,check_out=datetime.strftime(check_out,"%Y-%m-%d"),check_in=datetime.strftime(check_in,"%Y-%m-%d"))
            booking.save()

            messages.success(request,"Your Rooms are Booked")
            return redirect("/hotels/"+room_id+"/")
        else:
            messages.error(request,"Please make Login First")
            return redirect("loginProcess")
    else:
        return redirect("Home")