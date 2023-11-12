from django.urls import path
from . import views
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView

urlpatterns = [
    path('', EventListView.as_view() , name='events-home'),
    path('event/<int:pk>/', EventDetailView.as_view() , name='event-detail'),
    path('event/new/', EventCreateView.as_view() , name='event-create'),
    path('event/<int:pk>/update', EventUpdateView.as_view() , name='event-update'),
    path('event/<int:pk>/delete', EventDeleteView.as_view() , name='event-delete'),
    path('about/', views.about, name='events-about'),
]