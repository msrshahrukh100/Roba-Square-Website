from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from authentication.username import get_user_name
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save


# upload location for user profile pics
def upload_location_user(instance, filename) :
	return "users/%s/%s" % (instance.user.id, filename)

# class for storing user information 1-1 qith the default user model
class UserInformation(models.Model) :
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_information')
	change_profile_pic = models.ImageField(upload_to=upload_location_user,height_field='height_field',width_field='width_field',blank=True, null=True,default='default.jpg')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	date_of_birth = models.CharField(max_length=20,blank=True, null=True)
	phonenumber = models.CharField(max_length=15,blank=True, null=True)
	profession = models.CharField(max_length=100, blank=True, null=True)
	name_of_institute = models.CharField(max_length=200, blank=True, null=True)
	slug = AutoSlugField(populate_from='user',unique=True)
	
	def __unicode__(self) :
		return str(self.user.username)

	class Meta :
		verbose_name = "User Information"
		verbose_name_plural = "User Information"




@receiver(post_save, sender=User)
def UserInformationreceiver(sender, instance, **kwargs):
	UserInformation.objects.get_or_create(user=instance)
	






