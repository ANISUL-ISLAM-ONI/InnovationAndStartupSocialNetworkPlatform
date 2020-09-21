from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
  comment = models.ForeignKey(
    comment,
    default=1,
    on_delete=models.CASCADE
  )
  Instructor = models.ForeignKey(
    User,
    default=1,
    on_delete=models.CASCADE
  )
