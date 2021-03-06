from django.shortcuts import render, redirect, get_object_or_404
from shopping.models import Slider, Categories, ProductDescription
from allauth.account.forms import ChangePasswordForm, AddEmailForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import UserInfoForm,AddressForm
from .models import UserInformation, Addresses
from social.models import PicOfTheWeek

from django.http import HttpResponse

def home_page(request) :
	context = {"slider":Slider.objects.all(),
	"categories":Categories.objects.all(),
	"newproducts":ProductDescription.objects.filter(new_product=True).filter(has_logo=False),
	"cartcount":len(request.session.get('products',[])),
	"picoftheweek" : PicOfTheWeek.objects.filter(publish_it=True).order_by('-id').first()
	}
	return render(request,'index.html',context)


@login_required
def change_settings(request) :

	user = request.user
	userinfo = UserInformation.objects.filter(user=user).first()
	addresses = Addresses.objects.filter(user=user)
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
	addressform = AddressForm(request.POST or None)
	if request.method == 'POST' :
		# print "first name" + request.POST.get('first_name',"")
		# print userinfoform.is_valid()
		if userinfoform.is_valid():
			formdata = userinfoform.cleaned_data
			print formdata['profession']
			if userinfo :
				userinfo.date_of_birth=formdata['date_of_birth']
				userinfo.phonenumber=formdata['phonenumber']
				userinfo.profession=formdata['profession']
				userinfo.name_of_institute=formdata['name_of_institute']
				userinfo.save()
			else :
				instance = UserInformation(					
					user=user,
					date_of_birth=formdata['date_of_birth'],
					phonenumber=formdata['phonenumber'],
					profession=formdata['profession'],
					name_of_institute=formdata['name_of_institute']
				 	)
				instance.save()

			user.first_name = formdata['first_name']
			user.last_name = formdata['last_name'] 
			user.save()
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

	context = {
	'userinfoform' : userinfoform,
	'userinfo':userinfo,
	'addressform':addressform,
	'addresses' : addresses,
	}
	return render(request,'settings.html',context)



@login_required
def change_dp(request) :
	pic = request.FILES.get('ppic')
	if pic._size > 3 * 1024 * 1024 :
		return HttpResponse("<h3>The file size is greater than 3 MB. Please go back and upload a smaller file.</h3>")
	user = request.user
	userinfo = UserInformation.objects.filter(user=user).first()
	userinfo.change_profile_pic = request.FILES.get('ppic')
	userinfo.save()
	return redirect('social:myprofile')


@login_required
def change_privacy_settings(request) :
	user = request.user
	userinfo = UserInformation.objects.filter(user=user).first()
	userinfo.showrecentlyviewed = request.POST.get('recentlyviewed',False)
	userinfo.showfollowers = request.POST.get('followers',False)
	userinfo.showfollowing = request.POST.get('following',False)
	userinfo.showdob = request.POST.get('showdob',False)
	userinfo.save()
	response = {'type': 1,
			'msg' : "Changes Saved!"
			}
	return JsonResponse(response)


@login_required
def addaddress(request):
	user = request.user
	address = request.POST.get('address')
	city = request.POST.get('city')
	pincode = request.POST.get('pincode')
	nearest_landmark = request.POST.get('nearest_landmark')
	Addresses.objects.get_or_create(user=user,address=address,city=city,pincode=pincode,nearest_landmark=nearest_landmark) 
	return redirect('authentication:change_settings')



@login_required
def removeaddress(request,id=None) :
	instance = get_object_or_404(Addresses,id=id)
	instance.delete()
	return redirect('authentication:change_settings')

def viewextra(request,id) :
	if id == '1' :
		return render(request,'extras/aboutus.html',{})
	if id == '2' :
		return render(request,'extras/communityguidelines.html',{})
	if id == '3' :
		return render(request,'extras/returnexchange.html',{})
	if id == '4' :
		return render(request,'extras/shipping.html',{})
	if id == '5' :
		return render(request,'extras/help.html',{})
	if id == '6' :
		return render(request,'extras/disclaimer.html',{})
	if id == '7' :
		return render(request,'extras/termsofuse.html',{})
	if id == '8' :
		return render(request,'extras/privacy.html',{})

