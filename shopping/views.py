from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from productreviews.forms import Reviewform
from .models import Categories, ProductDescription, ProductRelationsForLogo, BulkOrders
from cart.models import Cart
from social.models import RecentlyViewed, Connections
from django.contrib.auth.models import User
from django.http import JsonResponse
from social.models import Likes
from django.contrib.auth.decorators import login_required
from notifications.signals import notify
from django.core.urlresolvers import reverse
from random import randint
from sorl.thumbnail import get_thumbnail
from notifications.signals import notify
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_page
# Create your views here.


@cache_page(60*60)
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

@never_cache
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


@never_cache
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
	'reviews' : instance.reviews.all(),
	'reviewcount' : instance.reviews.all().count(),
	}
	return render(request,'view.html',context)

@never_cache
@csrf_exempt
def search(request) :
	query = request.POST.get('query')
	categoryquery = Categories.objects.filter(category__startswith=query)
	categoryitems = []
	for i in categoryquery :
		c = i.category
		im = get_thumbnail(i.image, '100x100')
		iu = im.url
		u = i.get_absolute_url()
		temp = {'category':c,'url':u,'imageurl':iu}
		categoryitems.append(temp)

	productquery = ProductDescription.objects.filter(has_logo=False).filter(name__startswith=query)
	productitems = []
	for i in productquery :
		n = i.name
		img = i.prod.first().productimages.first().image
		im = get_thumbnail(img, '100x100')
		iu = im.url
		u = i.get_absolute_url()
		temp = {'name':n,'url':u,'imageurl':iu}
		productitems.append(temp)
		 
	return JsonResponse({'categoryitems':categoryitems,'productitems':productitems})


@never_cache
@csrf_exempt
def checkavailability(request) :
	size = request.POST.get('size',None)
	pid = request.POST.get('id',None)
	requirednumber = request.POST.get('requirednumber',None)
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

@never_cache
@login_required
def bulkorders(request) :
	if request.method == 'POST' :
		data = request.POST
		if data.get('product') == '1' :
			product = 'Polo T-shirt'
		elif data.get('product') == '2' :
			product = 'Hoody'
		elif data.get('product') == '3' :
			product = 'Round Neck T-shirt'
		elif data.get('product') == '4' :
			product = 'Coffee Mugs'
		pic = request.FILES.get('pic')
		obj, created = BulkOrders.objects.get_or_create(
			user=request.user,
			product=product,
			base=data.get('baseproduct'),
			quantity=data.get('quantity'),
			description=data.get('description'),
			phone=data.get('phone'),
			image=pic
			)
		verb = "Your bulk order has been received, we'll get back to you shortly."
		url = reverse("shopping:viewbulkorders")
		notify.send(request.user, recipient=request.user, verb=verb, url=url, imageurl=obj.image.url)
		return redirect('/')

	return render(request,'bulkorders.html',{})


@never_cache
@login_required
def viewbulkorders(request) :
	user = request.user
	context = {'bulkorders':BulkOrders.objects.filter(user=user).order_by('-id')}
	return render(request,'viewbulkorders.html', context)


@never_cache
@login_required
def deletebulkorder(request,id) :
	x = get_object_or_404(BulkOrders,id=id)
	x.delete()
	return redirect('shopping:viewbulkorders')