from django.contrib import admin
from . models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    # Function to create image thumbnails
    def thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="40" style="border-radius: 50%;" alt="">'.format(object.main_photo.url))
        except:
            pass

    thumbnail.short_description = 'Car Image'
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model','year', 'body_style', 'fuel_type', 'is_featured',)
    list_display_links = ('id', 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type',)
    list_filter = ('city', 'model', 'body_style', 'fuel_type',)

admin.site.register(Car, CarAdmin)