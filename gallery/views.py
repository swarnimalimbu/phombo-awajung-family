from django.shortcuts import render
from .models import Event, Photo
from django.shortcuts import get_object_or_404

def home_view(request):
    recent_photos = Photo.objects.order_by('-id')[:8]
    return render(request, 'home.html', {
        'recent_photos': recent_photos
    })

def gallery_view(request):
    year = request.GET.get('year')

    events = Event.objects.prefetch_related('photos').order_by('-year')

    if year:
        events = events.filter(year=year)

    years = Event.objects.values_list('year', flat=True).distinct().order_by('-year')

    return render(request, 'gallery/gallery.html', {
        'events': events,
        'years': years,
        'selected_year': year
    })

def about_view(request):
    return render(request, 'about.html')

def event_detail_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    photos = event.photos.all()

    return render(request, 'gallery/event_detail.html', {
        'event': event,
        'photos': photos
    })

import os
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings

def create_admin_once(request):
    token = request.GET.get("token")

    if token != os.environ.get("ADMIN_SETUP_TOKEN"):
        return HttpResponse("Unauthorized", status=401)

    if User.objects.filter(username="admin").exists():
        return HttpResponse("Admin already exists")

    User.objects.create_superuser(
        username="admin",
        email="admin@phomboawajung.com",
        password="ChangeThisPassword123"
    )

    return HttpResponse("Admin created successfully")
