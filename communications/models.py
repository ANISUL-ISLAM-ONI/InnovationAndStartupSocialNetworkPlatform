from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,default=1,on_delete=models.CASCADE,null=True)

class Comment(models.Model):
    text = models.TextField(default="awesome!")
    post = models.ForeignKey(Post,default=1,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
  
class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.SET_NULL,related_name = "+", null=True, blank=True)
    receiver = models.ForeignKey(User,on_delete=models.SET_NULL, related_name = "+",null=True, blank=True)
    message = models.CharField(max_length = 200)
    received_at = models.DateTimeField(auto_now_add=True)
