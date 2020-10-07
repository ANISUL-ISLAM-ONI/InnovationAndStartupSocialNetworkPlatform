from django.contrib import admin
from course.models import coursePost, coursePage, enroll

# Register your models here.

admin.site.register(coursePost)
admin.site.register(coursePage)
admin.site.register(enroll)
from django.contrib import admin
from . import models

# Register your models here.
