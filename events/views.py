from django.shortcuts import render
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

def home(request):
    events = { 'events' : Event.objects.all()}
    context= {'events': events}
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
    fields = ['title','content','date','image','link']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'content','date','image','link']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.organization:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.organization:
            return True
        return False
    
def about(request):
    return render(request, 'events/about.html', {'title': 'About'})


