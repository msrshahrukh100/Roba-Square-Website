from django.db import models
from django.contrib.auth.models import User
from shopping.models import ProductDescription
# Create your models here.

class OnlineTransactionsDetail(models.Model) :
	user = models.ForeignKey(User,related_name="online_transactions")
	amount = models.CharField(max_length=200)
	buyer = models.EmailField(max_length=200)
	buyer_name = models.CharField(max_length=200)
	buyer_phone = models.CharField(max_length=15,null=True,blank=True)
	currency = models.CharField(max_length=5)
	fees = models.CharField(max_length=100)
	longurl = models.URLField(max_length=200)
	mac = models.CharField(max_length=100)
	payment_id = models.CharField(max_length=150)
	payment_request_id = models.CharField(max_length=150)
	purpose = models.CharField(max_length=250)
	shorturl = models.URLField(max_length=100)
	status = models.CharField(max_length=10)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self) :
		return self.buyer

	class Meta:
		ordering = ['-id']


class BuyingCart(models.Model) :
	user = models.ForeignKey(User,related_name="user_bought_cart")
	product = models.ForeignKey(ProductDescription, related_name="buying_cart")
	size = models.CharField(max_length=5)
	quantity = models.CharField(max_length=3)
	price = models.CharField(max_length=20)
	address = models.CharField(max_length=150)
	phonenumber = models.CharField(max_length=15)
	method_of_payment = models.CharField(max_length=20)
	instamojo_request_id = models.CharField(max_length=150,null=True,blank=True) 
	cod_unique_id = models.CharField(max_length=150,null=True,blank=True) 
	status = models.CharField(max_length=10, default="Pending")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	invoice = models.FileField(blank=True,null=True)

	def __unicode__(self):
		return str(self.id)
	








