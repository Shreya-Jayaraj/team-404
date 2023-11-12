from django.urls import path
from . import views
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', EventListView.as_view() , name='events-home'),
    path('event/<int:pk>/', EventDetailView.as_view() , name='event-detail'),
    path('event/new/', EventCreateView.as_view() , name='event-create'),
    path('event/<int:pk>/update', EventUpdateView.as_view() , name='event-update'),
    path('event/<int:pk>/delete', EventDeleteView.as_view() , name='event-delete'),
    path('about/', views.about, name='events-about'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)