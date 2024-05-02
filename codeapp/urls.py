from django.contrib import admin
from django.urls import path
from codeapp import views



urlpatterns = [
    path("", views.index,name='codeapp'),
    path("about", views.about,name='about'),
    path("contact", views.contact,name='contact'),
]