from django.shortcuts import render
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = { 'events' : Event.objects.all()}
    return render(request,'events/home.html', context)

class EventListView(ListView):
    model = Event
    template_name = 'events/home.html'
    context_object_name = 'events'
    ordering = ['-date']

class EventDetailView(DetailView):
    model = Event

class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    fields = ['title','content','date']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'events/about.html', {'title': 'About'})
