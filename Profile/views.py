from django.shortcuts import render, redirect


# Create your views here.
def profile(request):
    return render(request, 'profile/profile.html')

