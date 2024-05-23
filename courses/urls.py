from tkinter import N
from django.urls import path , include 
from .views import * 

app_name = 'courses'


urlpatterns = [
    path('',courses_view,name='videos'),
    path('search/',video_search,name='search'),
]