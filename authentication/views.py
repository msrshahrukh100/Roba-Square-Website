from django.shortcuts import render
from shopping.models import Slider, Categories, ProductDescription
from allauth.account.forms import ChangePasswordForm, AddEmailForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import UserInfoForm
from .models import UserInformation


def home_page(request) :
	context = {"slider":Slider.objects.all(),
	"categories":Categories.objects.all(),
	"newproducts":ProductDescription.objects.filter(new_product=True),
	"cartcount":len(request.session.get('products',[]))
	}
	return render(request,'index.html',context)

@login_required
def change_settings(request) :

	user = request.user
	userinfo = UserInformation.objects.filter(user=user).first()

	data = {
	'first_name' : user.first_name,
	'last_name' : user.last_name,
	}

	if userinfo :
		data['phonenumber'] = userinfo.phonenumber
		data['date_of_birth'] = userinfo.date_of_birth
		data['profession'] = userinfo.profession
		data['name_of_institute'] = userinfo.name_of_institute

	userinfoform = UserInfoForm(request.POST or None,initial=data)
	if request.method == 'POST' :
		print "first name" + request.POST.get('first_name',"")
		# print userinfoform.is_valid()
		if userinfoform.is_valid():
			formdata = userinfoform.cleaned_data
			if userinfo : 
				UserInformation.objects.update(
					date_of_birth=formdata['date_of_birth'],
					phonenumber=formdata['phonenumber'],
					profession=formdata['profession'],
					name_of_institute=formdata['name_of_institute']
				 	)
			else :
				UserInformation.objects.create(					
					user=user,
					date_of_birth=formdata['date_of_birth'],
					phonenumber=formdata['phonenumber'],
					profession=formdata['profession'],
					name_of_institute=formdata['name_of_institute']
				 	)

			user.first_name = formdata['first_name']
			user.last_name = formdata['last_name']
			user.save()
			print "valid bhai"
			response = {'type': 1,
			'msg' : "Changes Saved!"
			}
			return JsonResponse(response)
		else :
			response = {
			'type' : 0,
			'errors' : userinfoform.errors 
			}
			return JsonResponse(response)

	# if userinfoform.is_valid() :
	# 	print "its valid"
	# else :
	# 	print "invalid"
	# 	print userinfoform.errors
	context = {
	'userinfoform' : userinfoform,
	# "cartcount":len(request.session.get('products',[])),
	}
	return render(request,'settings.html',context)

