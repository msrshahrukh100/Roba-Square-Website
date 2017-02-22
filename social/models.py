from django.db import models
from django.contrib.auth.models import User
from shopping.models import ProductDescription
from sorl.thumbnail import ImageField

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

class Likes(models.Model) :
	user = models.ForeignKey(User,related_name='userlikes')
	product = models.ForeignKey(ProductDescription, related_name='productlikes')
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.user.username


def upload_location_picoftheweek(instance,filename) :
	return "pic_of_the_week/%s/%s" % (instance.id, filename)

class PicOfTheWeek(models.Model) :
	user = models.ForeignKey(User,related_name='picoftheweek')
	description = models.CharField(max_length=300)
	image = ImageField(upload_to = upload_location_picoftheweek,height_field="height_field", width_field="width_field",help_text="Image for pic of the week")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	publish_it = models.BooleanField(default=False)

	def __unicode__(self) :
		return str(self.id)

	def get_fb_link(self) :
		return '/fb/'+str(self.id)+str(self.user.id)



