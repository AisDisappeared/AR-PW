import re
from django.shortcuts import render
from .models import video
# Create your views here.


def courses_view(request):
    videos = video.objects.all().order_by('id')
    
    # Increment views for each video
    for vid in videos:
        vid.views += 1
    
    # Bulk update all videos to save the incremented views
    video.objects.bulk_update(videos, ['views'])
    
    context = {"videos": videos}
    return render(request, 'courses/videos.html', context)