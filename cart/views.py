from django.shortcuts import render, redirect
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
	request.session['products'].remove(str(id))
	print request.session['products']
	return redirect('cart:viewcart')

def viewcart(request) :
	cart = request.session.get('products',None)
	products = []
	for i in cart :
		products.append(ProductDescription.objects.filter(id=int(i)).first())
	context = {
	'type':1,
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

