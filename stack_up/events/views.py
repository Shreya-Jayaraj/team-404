from django.shortcuts import render
from .models import Event

events = [
    {
        'organization': 'gec thrissur',
        'title': 'Event 1',
        'content': 'First event content',
        'date': 'August 27, 2018'
    },
    {
        'organisation': 'gec idukki',
        'title': 'Event 2',
        'content': 'Second event content',
        'date': 'August 28, 2018'
    }
]

def home(request):
    context = { 'events' : Event.objects.all()}
    return render(request,'events/home.html', context)

def about(request):
    return render(request,'events/about.html', {'title': 'About'})

#blog->templates->blog->templates.html
