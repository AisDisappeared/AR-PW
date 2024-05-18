from django.urls import path , include 
from .views import * 


urlpatterns = [
    path('',index_view,name="index"),
    path('contact',contact_view,name="contact"),
    path('about',about_view,name="about"),
]