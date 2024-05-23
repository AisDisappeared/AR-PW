from debug_toolbar import APP_NAME
from django.urls import path , include 
from .views import * 

app_name = 'website'


urlpatterns = [
    path('',index_view,name="index"),
    path('subscribe',subscribe_view , name="subscribe"),
]