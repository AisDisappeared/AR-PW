from django.shortcuts import render
from courses.models import video
from .forms import SubscribeForm
import sweetify

# Create your views here.


def index_view(request):
    videos = video.objects.all().order_by('id')[:4]
    # Increment views for each video
    for vid in videos:
        vid.views += 1
    
    # Bulk update all videos to save the incremented views
    video.objects.bulk_update(videos, ['views'])


    context = {"videos":videos}
    return render(request,'website/index.html',context)






def subscribe_view(request):
    if request.method == 'POST':
         form = SubscribeForm(request.POST)
         if form.is_valid():
            form.save()       
            sweetify.success(request,'Welcome to our community! Thank you for supporting',persistent = 'OK')
         else:
            sweetify.error(request,'an error occured',persistent = ':(')

      
    form = SubscribeForm(request.POST)
    context = {'form': form}
    return render(request , 'website/index.html',context)