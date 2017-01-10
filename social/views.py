from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Connections
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
	following = User.objects.filter(id=id).first()
	c, created = Connections.objects.get_or_create(user=user, following=following)
	if created :
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