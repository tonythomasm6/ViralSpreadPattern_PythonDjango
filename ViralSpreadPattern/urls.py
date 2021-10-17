
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('findPattern/', views.findPattern, name="findPattern"),
    path('load_people/',views.load_people, name="load_people")
]