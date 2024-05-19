from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class video(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True,blank=True)
    video = models.FileField(upload_to='videos/')
    tags = TaggableManager()
    views = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.title)
    
    class Meta:
        ordering = ['-published_date']