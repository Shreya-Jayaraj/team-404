from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'