"""serviceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .serviceapp import views
urlpatterns = [

    #admin
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('log/',views.log,name="log"),
    path('add_service_stations/', views.add_service_stations, name="add_service_stations"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('save_stations/',views.save_stations,name="save_stations"),
    path('add_service_head/', views.add_service_head, name="add_service_head"),
    path('save_head/',views.save_head,name="save_head"),
    path('view_stations/',views.view_stations,name="view_stations"),
    path('view_head/',views.view_head,name="view_head"),
    path('view_user/',views.view_user,name="view_user"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),


    #user
    path('user_reg/',views.user_reg,name="user_reg"),
    path('save_user/',views.save_user,name="save_user"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_log/',views.user_log,name="user_log"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('service/',views.service,name="service"),
    path('car/',views.car_list,name="car_list"),
    path('car_details/',views.car_details,name="car_details"),
    path('car_values/',views.car_values,name="car_values"),
    path('save_booking/',views.save_booking,name="save_booking"),
    path('book_details/',views.book_details,name="book_details"),
    path('approve_booking/',views.approve_booking,name="approve_booking"),
    path('reject/',views.reject,name="reject"),
    path('estimated_booking/',views.estimated_booking,name="estimated_booking"),
    path('started_booking/',views.started_booking,name="started_booking"),
    path('delivered_booking/',views.delivered_booking,name="delivered_booking"),
    path('update_review/',views.update_review,name="update_review"),
    path('user_home/',views.user_home,name="user_home"),



    #service head
    path('head_login/',views.head_login,name="head_login"),
    path('head_log/',views.head_log,name="head_log"),
    path('head_logout/',views.head_logout,name="head_logout"),
    path('add_person_details/',views.add_person_details,name="add_person_details"),
    path('save_person/',views.save_person,name="save_person"),
    path('add_feedback_details/',views.add_feedback_details,name="add_feedback_details"),
    path('save_feedback/',views.save_feedback,name="save_feedback"),
    path('view_bookings/',views.view_bookings,name="view_bookings"),
    path('update_pending/',views.update_pending,name="update_pending"),
    path('view_estimated_bookings/',views.view_estimated_bookings,name="view_estimated_bookings"),
    path('view_approved_bookings/',views.view_approved_bookings,name="view_approved_bookings"),
    path('view_started_bookings/',views.view_started_bookings,name="view_started_bookings"),
    path('view_completed_bookings/',views.view_completed_bookings,name="view_completed_bookings"),
    path('view_delivered_bookings/',views.view_delivered_bookings,name="view_delivered_bookings"),

]
