from django.db import models
from django.utils.timezone import now

# Create your models here.

#admin
from django.db.models.functions import datetime


class admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class add_servicestation(models.Model):
    station_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    License_number = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class add_servicehead(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateField()
    station_name = models.CharField(max_length=100)

    License_number = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


#user

class user_details(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateField()
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


#service head


class add_person(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateField()
    station_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)




class car(models.Model):
    vendor_name=models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    image_url=models.CharField(max_length=1500)

class booking(models.Model):
    car_id = models.IntegerField(max_length=100)
    user_id = models.IntegerField(max_length=100)
    purchase_date = models.DateField()
    problem = models.CharField(max_length=1000)
    status = models.CharField(max_length=100,default="pending")
    estimate = models.IntegerField(max_length=100,default=0)
    start_date = models.CharField(max_length=100,default=0)
    start_time = models.CharField(max_length=100,default=0)
    completion_date = models.CharField(max_length=100,default=0)
    actual_cost = models.IntegerField(max_length=100,default=0)
    delivery_date =models.CharField(max_length=100,default=0)
    review = models.CharField(max_length=100,default="SOME STRING")

