from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from productreviews.forms import Reviewform
from .models import Categories, ProductDescription, ProductRelationsForLogo
from cart.models import Cart
from social.models import RecentlyViewed, Connections
from django.contrib.auth.models import User
from django.http import JsonResponse
from social.models import Likes
from django.contrib.auth.decorators import login_required
from notifications.signals import notify
from django.core.urlresolvers import reverse
from random import randint
# Create your views here.


def view_category_or_item(request, qtype=None, slug=None) :
	if qtype == 'categories' :
		instance = Categories.objects.filter(slug=slug).first()
		products = instance.get_products_to_show.order_by('?')
		context = {
		'cname' : instance.category,
		'type':1,
		'products' : products,
		}
		return render(request,'view.html',context)
	elif qtype == 'product' :
		instance = ProductDescription.objects.filter(slug=slug).first()
		if instance.has_logo :
			raise Http404
		detailsofproduct = instance.productdetails.all()
		# create a entry on the recently viewed table
		user = request.user
		if not user.is_anonymous() : 
			c, created = RecentlyViewed.objects.get_or_create(user=user, product=instance)
			if not created :
				c.user = request.user
				c.save()
		data = {'product':instance.id}
		form = Reviewform(initial=data)
		likes = Likes.objects.filter(product=instance)
		likescount = likes.count()
		if request.user.is_anonymous() :
			recentlyviewed = []
			friendslikes = []
		else :
			ids = Connections.objects.values_list('following').filter(user=user)
			connections = User.objects.filter(id__in=ids).order_by("?")
			friendslikes = likes.filter(user__in=connections)
			recentlyviewed = RecentlyViewed.objects.filter(user=request.user)

		context = {
		'type' : 2,
		'detailp':instance,
		'detailsofproduct':detailsofproduct,
		'recentlyviewed':recentlyviewed[1:5],
		"form" : form,
		'likes' : likes,
		'likescount':likescount,
		'friendslikes' : friendslikes,
		'reviews' : instance.reviews.all(),
		'reviewcount' : instance.reviews.all().count(),
		}
		return render(request,'view.html',context)
	else :
		raise Http404

@login_required
def view_private_item(request,slug=None) :
	user = request.user
	instance = ProductDescription.objects.get(slug=slug)
	related_product = ProductRelationsForLogo.objects.get(product=instance)
	key = randint(100000,999999)
	request.session['privateproduct'] = key
	text = {'msg':'We will shortly notify you with the link to your customized product on Roba Square.'}
	url = reverse("shopping:show_private_item",kwargs={"slug":related_product.related_to.slug,"key":key})
	verb = "Click to see your customized product."
	imageurl = related_product.related_to.get_image_url
	notify.send(user, recipient=user, verb=verb, url=url, imageurl=imageurl)
	return JsonResponse(text)


@login_required
def show_private_item(request,slug=None,key=None) :
	if request.session.get('privateproduct')  != int(key) :
		return render(request,'error.html',{"error":"The link for your customized product expired!"})
	instance = ProductDescription.objects.get(slug=slug)
	detailsofproduct = instance.productdetails.all()
	user = request.user

	likes = Likes.objects.filter(product=instance)
	likescount = likes.count()
	ids = Connections.objects.values_list('following').filter(user=user)
	connections = User.objects.filter(id__in=ids).order_by("?")
	friendslikes = likes.filter(user__in=connections)
	data = {'product':instance.id}
	form = Reviewform(initial=data)

	context = {
	'type' : 2,
	'detailp':instance,
	'detailsofproduct':detailsofproduct,
	"form" : form,
	'likes' : likes,
	'likescount':likescount,
	'friendslikes' : friendslikes,
	}
	return render(request,'view.html',context)


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

	productquery = ProductDescription.objects.filter(has_logo=False).filter(name__startswith=query)
	productitems = []
	for i in productquery :
		n = i.name
		iu = i.get_image_url
		u = i.get_absolute_url()
		temp = {'name':n,'url':u,'imageurl':iu}
		productitems.append(temp)
		 
	return JsonResponse({'categoryitems':categoryitems,'productitems':productitems})



@csrf_exempt
def checkavailability(request) :
	size = request.POST.get('size',None)
	pid = request.POST.get('id',None)
	requirednumber = request.POST.get('requirednumber',None)
	# instance = ProductDescription.objects.get(id=)
	instance = get_object_or_404(ProductDescription, id=int(pid))
	productinstance = instance.prod.get(size=size)
	data = {}
	if productinstance :
		if productinstance.stockcount >= int(requirednumber) :
			data['type'] = 1
			data['msg'] = "Success"
		else : 
			data['type'] = 0
			data['msg'] = "Sorry, "+requirednumber + " pieces of this item is not available. Please try with different size or quantity."
	else :
		data['type'] = 0
		data['msg'] = "Sorry, this size is not available."
	return JsonResponse(data)
