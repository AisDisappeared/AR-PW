from django.contrib import admin
from .models import video
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date','views')
    list_filter = ('title',)
    empty_value_display = "-empty-"
    search_fields = ('title','description')
    save_as = True 
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'




admin.site.register(video,VideoAdmin)