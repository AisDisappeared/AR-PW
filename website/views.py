from django.shortcuts import render
from courses.models import video
# Create your views here.


def index_view(request):
    videos = video.objects.all()
    context = {"videos":videos}
    return render(request,'website/index.html',context)

def contact_view(request):
    return render(request,'website/contact.html')

def about_view(request):
    return render(request,'website/about.html')

