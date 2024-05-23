import re
from django.shortcuts import render
from .models import video
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def courses_view(request):
    videos = video.objects.all().order_by('id')
    
    # Increment views for each video
    for vid in videos:
        vid.views += 1
    
    # Bulk update all videos to save the incremented views
    video.objects.bulk_update(videos, ['views'])
      
    p = Paginator(videos,6)
    try:
        page_number = request.GET.get('page')
        videos = p.get_page(page_number)
    except EmptyPage:
        videos = videos.get_page(1)
    except PageNotAnInteger:
        videos = videos.get_page(1)


    context = {"videos": videos}
    return render(request, 'courses/videos.html', context)



