from django.shortcuts import render
from shopping.models import ProductDescription
from django.http import JsonResponse

# Create your views here.

def addtocart(request,id=None) :
	cart = request.session.get('products',None)
	print id
	if cart :
		print cart
		if id in cart :
			return JsonResponse({'msg':'This is already in cart!'})
		else:
			cart.append(id)
			request.session['products'] = cart
			return JsonResponse({'msg':'Added to cart!','count':len(request.session['products'])})
	else :
		request.session['products'] = []
		request.session['products'].append(id) 
		return JsonResponse({'msg':'Added to cart!','count':1})

	print request.session.get('products')

