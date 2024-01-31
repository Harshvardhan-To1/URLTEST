from django.contrib import admin
from django.urls import path,include
from W2 import views

app_name = 'W2'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('index',views.index,name = 'index'),
    path('present',views.present,name = 'present'),
    path('Records',views.Records,name = 'Records'),
    path('contact',views.contact,name = 'contact'),
    path('Home',views.Home,name = 'Home')
]