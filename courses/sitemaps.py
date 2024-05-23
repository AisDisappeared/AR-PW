from django.contrib import sitemaps
from django.urls import reverse


class VideosStatic(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["courses:videos"]

    def location(self, item):
        return reverse(item)



