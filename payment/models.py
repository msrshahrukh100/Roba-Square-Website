from django.db import models
from django.contrib.auth.models import User
from shopping.models import ProductDescription
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.conf import settings
from django.http import Http404
from instamojo_wrapper import Instamojo
from datetime import date, timedelta
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.core.mail import EmailMessage
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
	paymentid = models.CharField(max_length=150,null=True,blank=True)
	cod_unique_id = models.CharField(max_length=150,null=True,blank=True) 
	status = models.CharField(max_length=10, default="Pending")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	invoice_url = models.URLField(default='/')
	returned = models.BooleanField(default=False)
	delivered = models.BooleanField(default=False)
	def __unicode__(self):
		return str(self.id)

	def get_return_url(self) :
		return reverse("payment:returns" , kwargs={"id":self.id})


	@property
	def is_valid_return_date(self):
		if date.today() - timedelta(7) > self.timestamp.date():		
			return False
		return True

@receiver(pre_save, sender=BuyingCart)
def send_email_to_user(sender, instance, **kwargs):
	pass


    # Pass false so FileField doesn't save the model.
	# try:
	# # email = EmailMessage(
	# # subject='Hello',
	# # body='Body goes here',
	# # from_email='care@robasquare.com',
	# # to=['msr.concordfly@gmail.com'],
	# # headers={'Content-Type': 'text/plain'},
	# # )
	# # email.send()
	# except :
	# 	pass

    



class Refund_requests(models.Model) :
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='refundrequest')
	refund_item = models.ForeignKey(BuyingCart,on_delete=models.DO_NOTHING, related_name="refunds")
	reason = models.CharField(max_length=200)
	refund_amount_to_user = models.BooleanField(default=False,help_text="Setting this field to true refunds the amount to the user's account.Set it to true only after you receive the products")

	def __unicode__(self) :
		return str(self.id)

# for the online payment only
class RefundsHistory(models.Model) :
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='refundhistory')
	refundid = models.CharField(max_length=50)
	payment_id = models.CharField(max_length=150)
	status = models.CharField(max_length=20)
	refundtype = models.CharField(max_length=5)
	body = models.CharField(max_length=200)
	refund_amount = models.CharField(max_length=50)
	total_amount = models.CharField(max_length=50)
	created_at = models.CharField(max_length=100)


def refund_amount(sender, instance, **kwargs):
	if instance.refund_amount_to_user :
		if instance.refund_item.method_of_payment == "Online Payment" :
			print "online pay"
			try : 
				api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://www.instamojo.com/api/1.1/')
				api.refund_create(instance.refund_item.paymentid,"QFL",instance.reason,instance.refund_item.price)
				x = api.refund_detail(instance.refund_item.paymentid)
				if x.get('success') :
					refundid = x['refund'].get('id')
					payment_id = x['refund'].get('payment_id')
					status = x['refund'].get('status')
					refundtype = x['refund'].get('type')
					body = x['refund'].get('body')
					refund_amount = x['refund'].get('refund_amount')
					total_amount = x['refund'].get('total_amount')
					created_at = x['refund'].get('created_at')
					RefundsHistory.objects.get_or_create(
						user=instance.user,
						refundid=refundid,
						payment_id=payment_id,
						status=status,
						refundtype=refundtype,
						body=body,
						refund_amount=refund_amount,
						total_amount=total_amount,
						created_at=created_at)
				else :
					raise Http404
			except :
				raise Http404

pre_save.connect(refund_amount, sender=Refund_requests)


	








