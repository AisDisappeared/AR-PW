from django.urls import path , include 
from .views import * 


app_name = 'accounts'

urlpatterns = [
    path('login/',login_view,name="login"),
    path('signup/',register_view,name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
]