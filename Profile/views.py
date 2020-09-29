from django.shortcuts import render, redirect


# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('/')