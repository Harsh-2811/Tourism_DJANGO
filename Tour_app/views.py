from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
from blogs.models import Blog
# Create your views here.
def index(request):

    blogs = Blog.objects.filter(status="1").order_by('-date')[:3]
    countries = Countries.objects.all().order_by('id')
    packages = Tour_package.objects.filter(is_available=True).order_by('id')
    days= Tour_package.objects.values_list('no_of_days',flat=True)
    cost= Tour_package.objects.values_list('cost_per_person',flat=True)
    return render(request,"index.html",{'countries':countries,'packages':packages,'blogs':blogs,'days':days,'costs':cost})

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


