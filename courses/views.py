import re
from django.shortcuts import render
from .models import video
# Create your views here.


def courses_view(request):
    return render (request,'courses/videos.html')