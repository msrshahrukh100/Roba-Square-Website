from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Connections, RecentlyViewed, Likes
from authentication.models import UserInformation
from shopping.models import ProductDescription
from notifications.signals import notify
from authentication.username import get_user_name
# Create your views here.

@login_required
def viewallusers(request) :
	user = request.user
	# .filter(is_superuser=False).filter(is_staff=False)
	users = User.objects.order_by('-id')
	ids = Connections.objects.values_list('following').filter(user=user)
	connections = User.objects.filter(id__in=ids)
	context = {'users':users,'connections':connections}
	return render(request,'friends.html',context)

@login_required
def addconnection(request,id=None) :
	user = request.user
	url = user.user_information.get_absolute_url()
	imageurl = user.user_information.get_image_url()
	following = User.objects.filter(id=id).first()
	c, created = Connections.objects.get_or_create(user=user, following=following)
	if created :
		verb = get_user_name(user) + " followed you."
		notify.send(user, recipient=following, verb=verb, url=url, imageurl=imageurl)
		return JsonResponse({'msg':'Added to connections!'})
	else :
		return JsonResponse({'msg':'Already in your connections!'})


@login_required
def removeconnection(request,id=None) :
	user = request.user
	following = User.objects.filter(id=id).first()
	x = get_object_or_404(Connections,user=user,following=following)
	x.delete()
	return JsonResponse({'msg':'Removed from connections'})


@login_required
def myprofile(request) :
	user = request.user
	ids = Connections.objects.values_list('following').filter(user=user)
	connections = User.objects.filter(id__in=ids)
	recentlyviewed = RecentlyViewed.objects.filter(user=user)
	idsf = Connections.objects.values_list('user').filter(following=user)
	followers = User.objects.filter(id__in=idsf)
	notifications = user.notifications.all()
	context = {'user':user,'connections' : connections, 'recentlyviewed' : recentlyviewed,'notifications':notifications,'followers':followers}
	return render(request,'myprofile.html',context)

@login_required
def viewuser(request,slug=None) :
	loggedinuser = request.user
	x = get_object_or_404(UserInformation,slug=slug)
	user = x.user
	ids = Connections.objects.values_list('following').filter(user=user)
	connections = User.objects.filter(id__in=ids)
	idsf = Connections.objects.values_list('user').filter(following=user)
	followers = User.objects.filter(id__in=idsf)
	print followers
	print x.showfollowers
	recentlyviewed = RecentlyViewed.objects.filter(user=user)
	context = {}
	context['user'] = user
	if loggedinuser in connections :
		if x.showrecentlyviewed :
			context['recentlyviewed'] = recentlyviewed
		if x.showfollowers :
			context['followers'] = followers
 		if x.showfollowing :
			context['connections'] = connections

	return render(request,'myprofile.html',context)

@login_required
def readallnotifications(request) :
	user = request.user
	qs = user.notifications.unread()
	qs.mark_all_as_read()
	return JsonResponse({'msg':'Read all'})

@login_required
def likedislike(request, id=None) :
	user = request.user
	product = get_object_or_404(ProductDescription, id=id)
	l, created = Likes.objects.get_or_create(user=user, product=product)
	if created :
		idsf = Connections.objects.values_list('user').filter(following=user)
		followers = User.objects.filter(id__in=idsf)
		verb = get_user_name(user) + " liked a product"
		url = product.get_absolute_url()
		imageurl = product.get_image_url
		print imageurl
		print url
		for i in followers : 
			notify.send(user, recipient=i, verb=verb, url=url, imageurl=imageurl)
		return JsonResponse({'msg':'You liked this product'})
	l.delete()
	return JsonResponse({'msg':'You unliked this product'})



	