from django.urls import path
from .views import home_view, gallery_view, about_view,event_detail_view
from .views import create_admin_once

urlpatterns = [
    path('', home_view, name='home'),
    path('gallery/', gallery_view, name='gallery'),
    path('event/<int:event_id>/', event_detail_view, name='event_detail'),
    path('about/', about_view, name='about'),

]
