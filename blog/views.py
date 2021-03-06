try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post, PostViews,BlogSlider
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from social.models import RecentlyViewed


from django.core.cache import cache



@login_required
def post_create(request):
	cache.clear()
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()

		instance.url = request.build_absolute_uri(instance.get_absolute_url()) 
		instance.save()


		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "blog/post_form.html", context)


def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	user = request.user

	print request.session.session_key
	if not user.is_anonymous() :
		c,created = PostViews.objects.get_or_create(
			user=user,
			post=instance,
			ip=request.META['REMOTE_ADDR'],
			session=request.session.session_key
			)

	else :
		c,created = PostViews.objects.get_or_create(
			post=instance,
			ip=request.META['REMOTE_ADDR'],
			session=request.session.session_key
			)
	if request.user.is_anonymous() :
		recentlyviewed = RecentlyViewed.objects.all().order_by('?')[:4]
	else :
		recentlyviewed = RecentlyViewed.objects.filter(user=request.user)[:4]

	context = {
		"posts" : Post.objects.filter(publish_it=True).order_by('?')[:3] ,
		"title": instance.title,
		"instance": instance,
		'count' : PostViews.objects.filter(post=instance).count(),
		"recentlyviewed":recentlyviewed,
	}
	return render(request, "blog/post_detail.html", context)


def post_list(request):
	queryset_list = Post.objects.filter(publish_it=True).filter(draft=False) #.order_by("-timestamp")
	images = BlogSlider.objects.all().order_by('-id')
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 7) 
	nopages = paginator.num_pages
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	if not request.user.is_anonymous() :
		my_contributions = Post.objects.filter(user=request.user)
	else :
		my_contributions = []
	context = {
		"object_list": queryset, 
		"images" : images,
		"title": "List",
		"my_contributions" : my_contributions,
		"nopages" : [i for i in range(1,nopages+1)],
		"page_request_var": page_request_var,
	}
	return render(request, "blog/post_list.html", context)



def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "blog/post_form.html", context)



def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("blog:list")
