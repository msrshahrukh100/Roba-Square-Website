from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, get_object_or_404
from shopping.models import ProductDescription
from .models import Reviews, ProductSuggestions
from django.http import Http404
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_page
# Create your views here.
@never_cache
def addreview(request) :
	if request.method == 'POST' :
		id = request.POST.get('product',"")
		review = request.POST.get('review',"")
		rating = request.POST.get('rating',0)
		product = ProductDescription.objects.filter(id=id).first()
		Reviews.objects.create(user=request.user,product=product,review=review,rating=rating)
		# my_url = product.get_absolute_url()
		# cache.delete(my_url)

	if product.has_logo :
		return redirect('shopping:show_private_item' , slug=product.slug, key = request.session.get('privateproduct'))
	return redirect('shopping:view_category_or_item',qtype = 'product',slug=product.slug)

@never_cache
def deletereview(request, id=None) :
	x = get_object_or_404(Reviews, id=id)
	product = x.product
	slug = product.slug
	x.delete()
	return redirect('shopping:view_category_or_item',qtype = 'product',slug=slug)

@never_cache
def productsuggestion(request) :
	if request.method == 'POST' :
		user = request.user
		if user.is_anonymous() :
			user = None
		content = request.POST.get('suggestions',"")
		email = request.POST.get('email',"")
		ProductSuggestions.objects.create(user=user,content=content,email=email)
	else :
		raise Http404


	return JsonResponse({"msg":"Suggestion received!"})


