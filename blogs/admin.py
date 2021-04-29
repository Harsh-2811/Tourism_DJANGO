from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px">'.format(object.image.url))
    list_display = ('title','slug','author','thumbnail','status','created_at','updated_at','date')
    list_display_links = ('title','slug','thumbnail')
admin.site.register(Blog,BlogAdmin)