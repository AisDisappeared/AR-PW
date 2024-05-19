from django.urls import path , include 
from .views import * 


urlpatterns = [
    path('login/',login_view,name="login"),
    path('signup/',register_view,name="register"),
    path('logout/',logout_view,name="logout"),
]