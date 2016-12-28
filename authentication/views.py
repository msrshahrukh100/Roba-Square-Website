from django.shortcuts import render

# Create your views here.

def get_user_name(user) :
	if user.is_anonymous() :
		return ""
	if user.first_name and user.last_name :
		return user.first_name + " " + user.last_name
	return user.username

def home_page(request) :
	return render(request,'index.html',{})

