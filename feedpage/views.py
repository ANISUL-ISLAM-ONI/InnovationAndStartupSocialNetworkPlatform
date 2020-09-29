from django.shortcuts import render, HttpResponse

# Create your views here.

def feedHome(request):
	return render(request, "feedpage/postfeed.html")