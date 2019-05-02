[Page "Setting up the Models.py"]

While I was making the website RobaSquare.com for my college, I was not sure how to implement the add to cart feature for the website. I looked up on Stack overflow and after getting some inspiration I decided to implement it myself.
So I decided to store it in the db with `products`  and `user`  as a foreign key.

[Code "{'language': 'js'}"]

class Cart(models.Model) :
	user = models.ForeignKey(User,related_name='cart')
	products = models.ForeignKey(ProductDescription, related_name='incart')

	def __unicode__(self) :
		return self.user.username

	class Meta :
		verbose_name = "User's Cart"
        verbose_name_plural = "User's Cart"

[/Code]

[/Page]


[Page "Adding cart data to session"]

Next I wanted to store all the cart items to the session data, so that I can easily modify it.

[Code "{'language': 'python'}"]
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
[/Code]


I also did some operations when the user logs out. Both of these methods are controlled by the **user_logged_in** and **user_logged_out** signals.

[Code "{'language': 'js'}"]
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
[/Code]
[/Page]

[Page "How to add to the cart?"]

Now the time has come to add some code to the views.py file. The below code handles what actually should happen when a user clicks on add to cart button.

[Code "{'language': 'js'}"]
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
[/Code]
[/Page]