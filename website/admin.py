from django.contrib import admin
from .models import Subscribe
# Register your models here.

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)
    save_as = True
    save_on_top = True 