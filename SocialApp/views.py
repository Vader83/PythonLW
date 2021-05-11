from django.shortcuts import render

from django.db import IntegrityError

from django.http import HttpRequest

from .models import User, News



def index(request):
	return render(request,
			   'SocialApp/Index.html')


def log_in(request):
	return render(request,
			   'SocialApp/Log_In.html')


def sign_up(request):
	return render(request,
			   'SocialApp/Sign_Up.html')


def create_new_user(request):

	first_name = request.POST.get("user_first_name","")
	last_name = request.POST.get("user_last_name","")
	user_email = request.POST.get("user_email","")
	user_password = request.POST.get("user_password","")

	try:
	    User.objects.create(firstName = first_name, lastName = last_name, password = user_password, email = user_email)
	except IntegrityError:
	    return render(request,
			   'SocialApp/Sign_Up.html',
			   {"IntegrityError":"User with this email already exists"})

	return render(request,
			   'SocialApp/News.html')
	



def create_news(request):
	return render(request,
			   'SocialApp/Create_News.html')


def post_news(request):
	return true

def news(request):
	return render(request,
			   'SocialApp/News.html')