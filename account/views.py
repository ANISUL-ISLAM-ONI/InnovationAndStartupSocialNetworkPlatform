from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def  home(request) :
	return render(request, 'account/signup.html')

def signup(request) :
	if request.method == 'POST' :
		firstname = request.POST.get('firstname', '')
		lastname = request.POST.get('lastname', '')
		username = request.POST.get('username', '')
		email = request.POST.get('email', '')
		password = request.POST.get('password', '')
		confpassword = request.POST.get('confpassword', '')

		if password == confpassword :
			user = User.objects.create_user(first_name = firstname, last_name = lastname, password = password, email = email, username = username)
			user.save()

	return redirect('/')

def userLogin(request) :
	if request.method == "POST" :
		userName = request.POST.get('username', '')
		userPassword = request.POST.get('password', '')

		# if user account is exist or not
		user = authenticate(username = userName, password = userPassword)

		if user is not None :
			login(request, user)
			return HttpResponse('Logged in')
		else :
			return HttpResponse('Invalid credentials')
