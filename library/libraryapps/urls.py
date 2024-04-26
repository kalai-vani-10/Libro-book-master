from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home ),
    path('adduser/',views.adduser),
    path('addmember/',views.addmember,name="addmember"),
    path('back/',views.back),
    path('addbooks/',views.addbooks ),
    path('addbookitems/',views.addbookitems,name="addbookitems"),
    path('deletebooks/', views.deletebooks),
    path('deleteparticularbook/', views.deleteparticularbook, name='deleteparticularbook'),
    path('availbooks/',views.availbooks,name='availbooks'),
    path('issuebooks/',views.issuebooks ),
    path('issuedetails/',views.issuedetails,name='issuedetails'),
    path('viewissuedbooks/',views.viewissuedbooks,name='viewissuedbooks'),
    path('returnbookpage/',views.returnbookpage,name='returnbookpage'),
    path('returnbooks/',views.returnbooks,name='returnbooks'),    
]
   