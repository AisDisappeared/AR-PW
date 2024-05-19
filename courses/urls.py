from tkinter import N
from django.urls import path , include 
from .views import * 

app_name = 'courses'


urlpatterns = [
    path('videos/',courses_view,name='videos'),
]