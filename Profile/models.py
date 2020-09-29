from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    first_name = User.first_name
    last_name = User.last_name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Nothing", max_length=500)
    email = models.EmailField(max_length=50, blank=True)
    country = models.CharField(max_length=100, blank=True)
    follower = models.ManyToManyField(User, blank=True, related_name='Friends')
    phone_nmber = models.CharField(max_length=13, blank=True)
    image = models.ImageField(upload_to = 'user_image', default='image.png')
    avater = models.ImageField(default='avater.png', upload_to='avater')
    def __str__(self):
        return self.user.username
