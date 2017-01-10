from django.shortcuts import render, redirect, get_object_or_404
from shopping.models import ProductDescription
from django.http import JsonResponse
from .models import Wishlist

# Create your views here.

def addtocart(request,id=None) :
	cart = request.session.get('products',None)
	if cart :
		if id in cart :
			return JsonResponse({'msg':'Already in your cart!'})
		else:
			cart.append(id)
			request.session['products'] = cart
			return JsonResponse({'msg':'Added to cart!','count':len(request.session['products'])})
	else :
		request.session['products'] = []
		request.session['products'].append(id) 
		return JsonResponse({'msg':'Added to cart!','count':1})

def deletefromcart(request,id=None) :
	cart = request.session['products']
	cart.remove(str(id))
	request.session['products'] = cart
	print request.session['products']
	return redirect('cart:viewcart')

def viewcart(request) :
	cart = request.session.get('products',None)
	print cart
	products = []
	for i in cart :
		products.append(ProductDescription.objects.filter(id=int(i)).first())
	context = {
	'type':1,
	'etype':1,
	'products' : products,
	'incart' : True,
	"cartcount":len(request.session.get('products',[]))
	}
	return render(request,'view.html',context)


def addtowishlist(request, id=None) :
	user = request.user
	product = ProductDescription.objects.filter(id=id).first()
	wl, created = Wishlist.objects.get_or_create(user=user, products=product)
	if created :
		return JsonResponse({'msg' : 'Added to wishlist'})
	else :
		return JsonResponse({'msg' : 'Already in your wishlist'})


def viewwishlist(request) :
	user = request.user
	products = []
	wishlist = Wishlist.objects.filter(user=user)
	for p in wishlist :
		products.append(p.products)

	context = {
	'type':1,
	'etype':2,
	'products' : products,
	'inwl' : True,
	"cartcount":len(request.session.get('products',[]))
	}
	return render(request,'view.html',context)


def deletefromwishlist(request, id=None) :
	product = ProductDescription.objects.filter(id=id).first()
	user = request.user
	x = get_object_or_404(Wishlist,user=user, products=product)
	x.delete()
	return redirect('cart:viewwishlist')