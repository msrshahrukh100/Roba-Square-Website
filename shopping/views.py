from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from productreviews.forms import Reviewform
from .models import Categories, ProductDescription
from social.models import RecentlyViewed
from django.http import JsonResponse
# Create your views here.


def view_category_or_item(request, qtype=None, slug=None) :
	if qtype == 'categories' :
		instance = Categories.objects.filter(slug=slug)
		products = instance.first().products_desc.all().order_by('?')
		context = {
		'cname' : instance.first().category,
		'type':1,
		'products' : products,
		}
		return render(request,'view.html',context)
	elif qtype == 'product' :
		instance = ProductDescription.objects.filter(slug=slug).first()
		# create a entry on the recently viewed table
		user = request.user
		if not user.is_anonymous() : 
			c, created = RecentlyViewed.objects.get_or_create(user=user, product=instance)
			if not created :
				c.user = request.user
				c.save()
		data = {'product':instance.id}
		form = Reviewform(initial=data)
		if request.user.is_anonymous() :
			recentlyviewed = []
		else :
			recentlyviewed = RecentlyViewed.objects.filter(user=request.user)
		context = {
		'type' : 2,
		'detailp':instance,
		'recentlyviewed':recentlyviewed[1:5],
		"form" : form,
		}
		return render(request,'view.html',context)
	else :
		raise Http404

@csrf_exempt
def search(request) :
	query = request.POST.get('query')
	categoryquery = Categories.objects.filter(category__startswith=query)
	categoryitems = []
	for i in categoryquery :
		c = i.category
		iu = i.image.url
		u = i.get_absolute_url()
		temp = {'category':c,'url':u,'imageurl':iu}
		categoryitems.append(temp)

	productquery = ProductDescription.objects.filter(name__startswith=query)
	productitems = []
	for i in productquery :
		n = i.name
		iu = i.get_image_url
		u = i.get_absolute_url()
		temp = {'name':n,'url':u,'imageurl':iu}
		productitems.append(temp)
		 
	return JsonResponse({'categoryitems':categoryitems,'productitems':productitems})



