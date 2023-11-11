from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now().date)
    organization = models.ForeignKey(User, on_delete=models.CASCADE)

