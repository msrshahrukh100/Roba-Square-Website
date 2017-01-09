from django.shortcuts import render
from django.http import Http404

from productreviews.forms import Reviewform
from .models import Categories, ProductDescription
# Create your views here.


def view_category_or_item(request, qtype=None, slug=None) :
	if qtype == 'categories' :
		instance = Categories.objects.filter(slug=slug)
		products = instance.first().products_desc.all().order_by('?')
		context = {
		'type':1,
		'products' : products,
		"cartcount":len(request.session.get('products',[]))
		}
		return render(request,'view.html',context)
	elif qtype == 'product' :
		instance = ProductDescription.objects.filter(slug=slug).first()
		data = {'product':instance.id}
		form = Reviewform(initial=data)
		context = {
		'type' : 2,
		'detailp':instance,
		"cartcount":len(request.session.get('products',[])),
		"form" : form,
		}
		return render(request,'view.html',context)
	else :
		raise Http404



