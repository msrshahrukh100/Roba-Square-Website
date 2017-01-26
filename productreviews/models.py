from django.db import models
from shopping.models import ProductDescription
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
class Reviews(models.Model) :
	user = models.ForeignKey(User, related_name='userreviews')
	product = models.ForeignKey(ProductDescription, related_name='reviews')
	review = models.TextField(blank=True,null=True)
	rating = models.PositiveIntegerField(blank=True,null=True)

	def __unicode__(self) :
		return str(self.product.name)

	@property
	def get_delete_review_url(self) :
		return reverse('review:deletereview', kwargs={"id":self.id})

	class Meta :
		verbose_name = "Reviews of Products"
		verbose_name_plural = "Reviews of Products"
		ordering = ['-id']



class ProductSuggestions(models.Model) :
	user = models.ForeignKey(User, related_name='suggestions', null=True)
	content = models.TextField()
	email = models.EmailField(null=True, blank=True)

	def __unicode__(self) :
		return str(self.id)


	class Meta :
		verbose_name = "Product Suggestion"
		verbose_name_plural = "Product Suggestions"




	