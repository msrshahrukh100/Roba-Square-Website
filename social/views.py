from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Connections, RecentlyViewed, Likes, PicOfTheWeek
from authentication.models import UserInformation
from shopping.models import ProductDescription
from notifications.signals import notify
from authentication.username import get_user_name
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from sorl.thumbnail import get_thumbnail
from authentication.username import get_user_name
from django.views.decorators.csrf import csrf_exempt
from notifications.signals import notify
from blog.models import Post


# Create your views here.
@login_required
def viewallusers(request) :
	user = request.user
	# .filter(is_superuser=False).filter(is_staff=False)
	users = User.objects.all().filter(is_superuser=False).filter(is_staff=False).order_by('?')

	paginator = Paginator(users, 24) 
	nopages = paginator.num_pages
	page_request_var = "people"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	ids = Connections.objects.values_list('following').filter(user=user)
	connections = User.objects.filter(id__in=ids)
	context = {'users':queryset,'connections':connections,'page_request_var':page_request_var,"nopages" : [i for i in range(1,nopages+1)],}
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
	notifications = user.notifications.all()[:10]
	my_contributions = Post.objects.filter(user=request.user)
	context = {'user':user,'connections' : connections, 'recentlyviewed' : recentlyviewed,'notifications':notifications,'followers':followers,'my_contributions':my_contributions}
	return render(request,'myprofile.html',context)



@login_required
def showallnotifications(request) :
	user = request.user
	notifications = user.notifications.all()
	context = {'notifications':notifications}
	return render(request,'notifications.html',context)


@login_required
def deletehistory(request) :
	user = request.user
	rv = RecentlyViewed.objects.filter(user=user)
	for i in rv :
		i.delete()
	return redirect('social:myprofile')

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
	context['my_contributions'] = Post.objects.filter(user=user).filter(publish_it=True)

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



@csrf_exempt
def search(request) :
	query = request.POST.get('query')
	peoplequery = User.objects.filter(
		Q(first_name__icontains=query)|
		Q(last_name__icontains=query)|
		Q(email__icontains=query)
		)[:6]
	
	searchusers = []
	for i in peoplequery :
		if i.socialaccount_set.all().first() :
			iu = i.socialaccount_set.all().first().get_avatar_url()
		else :
			iu = get_thumbnail(i.user_information.change_profile_pic, '100x100').url
		name = get_user_name(i)
		print i.user_information.profession
		print i.user_information.name_of_institute
		print i.user_information.profession != ""
		if (i.user_information.profession == None or i.user_information.name_of_institute == None):
			about = ""
		elif  (i.user_information.profession != "" ) and (i.user_information.name_of_institute != "") :
			about = str(i.user_information.profession) + " at " +str(i.user_information.name_of_institute)
		else :
			about = ""
		url = i.user_information.get_absolute_url()
		temp = {'name':name,'imageurl':iu,'about':about,'url':url}
		searchusers.append(temp)
		 
	return JsonResponse({'searchusers':searchusers})


@login_required
def addpicofweek(request) :
	if request.method == 'POST' :
		obj, created = PicOfTheWeek.objects.get_or_create(
			user=request.user,
			description = request.POST.get('description'),
			image = request.FILES.get('pic')
			)
		if created :
			verb = "Thank You for sending your pic. We will publish it shortly."
			url = '/'
			notify.send(request.user, recipient=request.user, verb=verb, url=url, imageurl=obj.image.url)
	return redirect("/")


def viewpicofweek(request) :
	context = {'pics': PicOfTheWeek.objects.filter(publish_it=True)}
	return render(request,'viewpicofweek.html',context)
