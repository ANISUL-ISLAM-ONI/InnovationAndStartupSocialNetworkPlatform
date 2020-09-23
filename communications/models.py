from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
    User,
    default=1,
    on_delete=models.CASCADE,
    null=True
  )
 class Comment(models.Model):
  text = models.TextField(default="awesome!")
  post = models.ForeignKey(
    Post,
    default=1,
    on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
    User,
    default=1,
    on_delete=models.CASCADE
  )
  
  class Message(models.Model):
	sender = models.Foreignkey(
        User,
        related_name = "sender_user"
    )
	receiver = models.Foreignkey(
        User,
        related_name = "receiver_user"
    )
	message = models.CharField(max_length = 200)
	received_at = models.DateTimeField(auto_now_add=True)
