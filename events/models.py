from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date = models.DateField()
    link = models.URLField(max_length=200,default='https://forms.gle/BXKTFjTNGekH4S7q9')
    organization = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'events_pics')
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk':self.pk})
