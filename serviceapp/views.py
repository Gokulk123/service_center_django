from django.contrib.sessions.models import Session
from django.shortcuts import render
from .models import admin
from .models import add_servicestation
from .models import add_servicehead
from .models import user_details
from .models import add_person
from .models import feedback
from .models import car
from .models import booking
from django.http import JsonResponse
# Create your views here.
#admin
def index(request):
    return render(request,'index.html',{})
def admin_login(request):
    return render(request,'admin_login.html',{})
def user_home(request):
    uname = request.session['user']
    return render(request,'user_home.html',{'user':uname})
def admin_home(request):
    return render(request,'admin_home.html',{'aname':request.session['admin']})
def log(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    ad = admin.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['admin'] = x.username
            return render(request, 'admin_home.html', {'aname': x.username})
    return render(request, 'admin_login.html', {'msg': "Incorrect username or password.Try again"})

def add_service_stations(request):

    return render(request,'add_service_stations.html',{})



def save_stations(request):
    db = add_servicestation(station_name=request.POST.get('sname'),
                      place=request.POST.get('place'), License_number=request.POST.get('lnum'),
                      username=request.POST.get('uname'), password=request.POST.get('pass'))

    db.save()
    return render(request, 'add_service_stations.html', {'msg': "Successfully Inserted"})


def add_service_head(request):
    stations = add_servicestation.objects.all()
    return render(request,'add_service_head.html',{'stations':stations})


def save_head(request):
    db = add_servicehead(name=request.POST.get('name'),place=request.POST.get('place'),date=request.POST.get('dob'), station_name=request.POST.get('sname'), License_number=request.POST.get('lnum'),username=request.POST.get('uname'), password=request.POST.get('pass'))

    db.save()
    return render(request, 'add_service_head.html', {'msg': "Successfully Inserted"})


def view_stations(request):
    stations = add_servicestation.objects.all()
    return render(request, 'view_stations.html', {'stations': stations})


def view_head(request):
    head = add_servicehead.objects.all()
    return render(request, 'view_head.html', {'head': head})

def view_user(request):
    user = user_details.objects.all()
    return render(request, 'view_user.html', {'user': user})


def admin_logout(request):
    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['admin'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'admin_login.html')


#user
def user_reg(request):
    return render(request,'user_reg.html',{})

def save_user(request):
    db = user_details(name=request.POST.get('name'),
                      place=request.POST.get('place'), date=request.POST.get('dob'),email=request.POST.get('email'),
                      username=request.POST.get('uname'), password=request.POST.get('pass'))

    db.save()
    return render(request, 'user_reg.html', {'msg': "Successfully Inserted"})


def user_login(request):
    return render(request, 'user_login.html', {})


def user_log(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    ad = user_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['user'] = x.username

            return render(request, 'user_home.html', {'user': x.username})
    return render(request, 'user_login.html', {'msg': "Incorrect username or password.Try again"})


def user_logout(request):
    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['user'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'user_login.html')


def service(request):
    #ad = car.objects.all()
    uname = request.session['user']
    return render(request,'service.html',{'user':uname})

def car_values(request):
    #ad = car.objects.all()
    uname = request.session['user']
    ad = user_details.objects.get(username=uname)
    return render(request,'car_values.html',{'user':uname,'ad':ad})

def car_list(request):

    ad = car.objects.all()
    cars = []
    for row in ad:
        tempComment = {}

        tempComment['id'] = row.id
        tempComment['vendor_name'] = row.vendor_name
        tempComment['model_name'] = row.model_name
        tempComment['image_url'] = row.image_url
        cars.append(tempComment)
    return JsonResponse(cars, safe=False)

def car_details(request):
    car_id = request.GET['id']
    ad = car.objects.get(id=car_id)
    cars = []

    tempComment = {}

    tempComment['id'] = ad.id
    tempComment['vendor_name'] = ad.vendor_name
    tempComment['model_name'] = ad.model_name
    tempComment['image_url'] = ad.image_url
    cars.append(tempComment)
    return JsonResponse(cars, safe=False)


def save_booking(request):
    uname = request.session['user']
    db = booking(car_id=request.POST.get('id'),user_id=request.POST.get('u_id'), purchase_date=request.POST.get('date'), problem=request.POST.get('problem'))
    db.save()
    return render(request, 'service.html', {'msg': "Successfully Booked",'user':uname})


def book_details(request):
    uname = request.session['user']
    user = user_details.objects.get(username=uname)
    book = booking.objects.filter(user_id=user.id)
    return render(request, 'booked_details.html', {'book': book,'user':uname})

def estimated_booking(request):
    uname = request.session['user']
    user = user_details.objects.get(username=uname)
    book = booking.objects.filter(user_id=user.id,status='Estimated')
    return render(request, 'booked_details.html', {'book': book,'user':uname})

def started_booking(request):
    uname = request.session['user']
    user = user_details.objects.get(username=uname)
    book = booking.objects.filter(user_id=user.id,status='Started')
    return render(request, 'booked_details.html', {'book': book,'user':uname})

def approve_booking(request):
    obj = booking.objects.get(id=request.POST.get('id'))
    #print(request.POST.get('id'))
    if obj.status == 'Estimated':
       obj.status = 'Approved'
    obj.save()
    uname = request.session['user']
    user = user_details.objects.get(username=uname)
    book = booking.objects.filter(user_id=user.id, status='Estimated')
    return render(request, 'booked_details.html', {'book': book,'user':uname})

def reject(request):
    obj = booking.objects.get(id=request.POST.get('id'))
    # print(request.POST.get('id'))
    obj.status = 'Reject'
    obj.save()
    uname = request.session['user']
    user = user_details.objects.get(username=uname)
    book = booking.objects.filter(user_id=user.id, status='Estimated')
    return render(request, 'booked_details.html', {'book': book,'user':uname})
def delivered_booking(request):
    uname = request.session['user']
    book = booking.objects.filter(status='Delivered')
    return render(request, 'booked_details.html', {'book': book,'user':uname})
def update_review(request):
    uname = request.session['user']
    obj = booking.objects.get(id=request.POST.get('id'))
    if obj.status == 'Delivered':
        obj.review = request.POST.get('review')
    obj.save()
    book = booking.objects.filter(status='Delivered')
    return render(request, 'booked_details.html', {'msg': 'Successfully Updated','book': book,'user':uname})


#service head

def head_login(request):
    return render(request, 'head_login.html', {})


def head_log(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    ad = add_servicehead.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['head'] = x.username
            return render(request, 'head_home.html', {'head': x.username})
    return render(request, 'head_login.html', {'msg': "Incorrect username or password.Try again"})

def head_logout(request):
    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['head'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'head_login.html')


def add_person_details(request):
    uname = request.session['head']
    ad = add_servicehead.objects.get(username = uname)
    return render(request, 'add_person.html', {'ad':ad})


def save_person(request):
    db = add_person(name=request.POST.get('name'),place=request.POST.get('place'),date=request.POST.get('dob'), station_name=request.POST.get('station'),username=request.POST.get('uname'), password=request.POST.get('pass'))

    db.save()
    return render(request, 'add_person.html', {'msg': "Successfully Inserted"})


def add_feedback_details(request):
    uname = request.session['head']
    ad = add_servicehead.objects.get(username=uname)
    return render(request, 'add_feedback.html', {'ad':ad})

def save_feedback(request):
    uname = request.session['head']
    ad = add_servicehead.objects.get(username=uname)
    db = feedback(name=request.POST.get('name'),feedback=request.POST.get('feedback'))

    db.save()
    return render(request, 'add_feedback.html', {'msg': "Successfully Inserted",'ad':ad})

def view_bookings(request):
    book = booking.objects.filter(status='pending')
    return render(request, 'view_booking.html', {'book': book})
def view_estimated_bookings(request):
    book = booking.objects.filter(status='Estimated')
    return render(request, 'view_booking.html', {'book': book})
def view_approved_bookings(request):
    book = booking.objects.filter(status='Approved')
    return render(request, 'view_booking.html', {'book': book})
def view_started_bookings(request):
    book = booking.objects.filter(status='Started')
    return render(request, 'view_booking.html', {'book': book})
def view_completed_bookings(request):
    book = booking.objects.filter(status='Completed')
    return render(request, 'view_booking.html', {'book': book})
def view_delivered_bookings(request):
    book = booking.objects.filter(status='Delivered')
    return render(request, 'view_booking.html', {'book': book})

def update_pending(request):
    from datetime import date
    from datetime import datetime
    obj = booking.objects.get(id=request.POST.get('id'))
    if obj.status == 'pending':
       obj.estimate = request.POST.get('estimate')
       obj.status = 'Estimated'
    elif obj.status == 'Estimated':
       obj.estimate = request.POST.get('estimate')
       obj.status = 'Estimated'
    elif obj.status == 'Approved':
        obj.status = 'Started'
        obj.start_date = date.today()
        obj.start_time = datetime.now().time()
    elif obj.status == 'Started':
        obj.actual_cost = request.POST.get('actual_cost')
        obj.completion_date = date.today()
        obj.status = 'Completed'
    elif obj.status == 'Completed':
        obj.delivery_date = date.today()
        obj.status = 'Delivered'
    obj.save()
    book = booking.objects.filter(status='pending')
    return render(request, 'view_booking.html', {'msg': 'Successfully Updated', 'book': book})









