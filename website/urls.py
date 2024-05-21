from debug_toolbar import APP_NAME
from django.urls import path , include 
from .views import * 

app_name = 'website'


urlpatterns = [
    path('',index_view,name="index"),
    path('contact',contact_view,name="contact"),
    path('about',about_view,name="about"),
    path('subscribe',subscribe_view , name="subscribe"),
]