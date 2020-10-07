from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.courseHome, name='coursehome'),
    path('post', views.post, name='post'),
    path("<int:courseId>", views.delCourse, name='delcourse'),
]