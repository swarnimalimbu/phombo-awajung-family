from django.contrib import admin
from .models import Event, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ('image', 'caption', 'contributor')
    show_change_link = True

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    inlines = [PhotoInline]
