from django.db import models
from django.contrib.auth.models import User
from shopping.models import ProductDescription
from django.contrib.auth.signals import user_logged_in, user_logged_out


# Create your models here.
class Cart(models.Model) :
	user = models.ForeignKey(User,related_name='cart')
	products = models.ForeignKey(ProductDescription, related_name='incart')

	def __unicode__(self) :
		return self.user.username

	class Meta :
		verbose_name = "User's Cart"
		verbose_name_plural = "User's Cart"



class Wishlist(models.Model) :
	user = models.ForeignKey(User,related_name='wishlist')
	products = models.ForeignKey(ProductDescription, related_name='inwishlist')

	def __unicode__(self) :
		return self.user.username

	class Meta :
		verbose_name = "User's Wishlist"
		verbose_name_plural = "User's Wishlist"


		
 




def user_logged_in_receiver(sender, user, request, **kwargs):
	cart = request.session.get('products',None)
	if not cart :
		request.session['products'] = []
		cart = []

	items = Cart.objects.filter(user=request.user)
	# add products from cart model to session
	for item in items :
		if str(item.products.id) not in cart :
			cart.append(str(item.products.id)) 

	request.session['products'] = cart

user_logged_in.connect(user_logged_in_receiver)


def user_logged_out_receiver(sender, user, request, **kwargs):
	cart = request.session.get('products',None)
	user = request.user
	print Cart.objects.filter(user=user)
	for j in Cart.objects.filter(user=user) :
		j.delete()

	print Cart.objects.all()

	if cart :
		for i in cart :
			x = ProductDescription.objects.filter(id=i).first()
			Cart.objects.create(user=user,products=x)

	request.session.clear()


user_logged_out.connect(user_logged_out_receiver)






