from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'is_enabled', 'long_url', 'time_create', 'time_update')
    list_display_links = ('short_url',)
    search_fields = ('short_url', 'long_url')
    list_editable = ('is_enabled',)


admin.site.register(Link, LinkAdmin)
