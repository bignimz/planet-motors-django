from django.contrib import admin
from .models import Team, Topbar
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    # Function to create image thumbnails
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%;" alt="">'.format(object.photo.url))

    thumbnail.short_description = 'Image'
    
    # Tuple to display teams in a table format
    list_display = ('id', 'thumbnail','first_name', 'designation', 'created_date')

    # Tuple to make team id and first_name clickable links
    list_display_links = ('id','first_name', 'thumbnail',)

    # Tuple to add a search functionality to team
    search_fields = ('first_name','last_name', 'designation',)

    # Tuple to display filter for teams by designation on the sidebar
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Topbar)
