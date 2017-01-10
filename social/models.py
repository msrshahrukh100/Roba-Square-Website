from django.db import models
from django.contrib.auth.models import User
from shopping.models import ProductDescription

# Create your models here.

class Connections(models.Model) :
	user = models.ForeignKey(User, related_name='socialuser')
	following = models.ForeignKey(User, related_name='following')

	def __unicode__(self):
		return self.user.username

	class Meta :
		unique_together = (('user','following'))
		verbose_name = "Connection"
		verbose_name_plural = "Connections"


class RecentlyViewed(models.Model) :
	user = models.ForeignKey(User,related_name='recentlyviewed')
	product = models.ForeignKey(ProductDescription, related_name='rvproducts')
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.user.username

	class Meta :
		unique_together = (('user','product'))
		verbose_name = "Recently Viewed"
		verbose_name_plural = "Recently Viewed"
		ordering = ['-timestamp']




