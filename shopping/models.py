from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse



# upload location for the image upload on categories
def upload_location_cat(instance, filename) :
	return "category_images/%s/%s" % (instance.category, filename)

# class for storing the cateogry of products
class Categories(models.Model):
	category = models.CharField(max_length = 200)
	image = models.ImageField(upload_to=upload_location_cat, width_field="width_field", height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	category_description = models.TextField(max_length=400)
	slug = AutoSlugField(populate_from='category',unique=True)
	link_text = models.CharField(max_length=100)

	def __unicode__(self) :
		return self.category


	def get_absolute_url(self):
		return reverse("shopping:view_category_or_item", kwargs={"slug": self.slug,"qtype":"categories"})





#class for storing the product description 
class ProductDescription(models.Model) :
	gender_opt = (('Male','Male'),('Female','Female'),('Unisex','Unisex'),('0','N/A'))

	category = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True,blank=True, related_name="products_desc")
	name = models.CharField(max_length = 250)
	description = models.TextField(blank=True, null=True)
	price = models.PositiveIntegerField()
	stockcount = models.PositiveIntegerField(default=0)
	gender = models.CharField(max_length=10, choices=gender_opt)
	new_product = models.BooleanField(default=False)
	slug = AutoSlugField(populate_from='name',unique=True)

	def __unicode__(self) :
		return self.name

	def get_absolute_url(self):
		return reverse("shopping:view_category_or_item", kwargs={"slug": self.slug,"qtype":"product"})

	@property
	def get_image_url(self) :
		return self.prod.first().productimages.first().image.url

	@property
	def get_add_to_cart_url(self) :
		return reverse("cart:addtocart", kwargs={"id":self.id})






#class for storing the list of all products with the variation of size and color
class Products(models.Model) :
	size_opt = (('S','S'),('M','M'),('L','L'),('XL','XL'),('XXL','XXL'),('0','N/A'))

	product = models.ForeignKey(ProductDescription,on_delete=models.CASCADE, null=True, related_name="prod")
	size = models.CharField(max_length=5, choices=size_opt)
	color = models.CharField(max_length=30)
	stockcount = models.PositiveIntegerField(default=0)

	def __unicode__(self) :
		return str(self.id)

	@property
	def get_image_url(self) :
		return self.productimages.first().image.url


#upload location for product images
def upload_location_pro(instance,filename) :
	return "product_images/%s/%s" % (instance.product.productimages.name, filename)

#class for storing the product images
class ImagesOfProducts(models.Model) :
	product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='productimages')
	image = models.ImageField(upload_to = upload_location_pro,height_field="height_field", width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	def __unicode__(self) :
		return str(self.id)

def upload_location_sli(instance,filename) :
	return "slider_images/%s"%(filename)

class Slider(models.Model) :
	view_opt = (('center','center'),('left','left'),('right','right'))

	image = models.ImageField(upload_to = upload_location_sli, null=False, blank=False ,height_field="height_field", width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	header = models.CharField(max_length=100)
	content = models.CharField(max_length=150)
	link_text = models.CharField(max_length=100)
	link = models.URLField(max_length=200)
	alignment = models.CharField(max_length=10 ,choices=view_opt, default="left")

	def __unicode__(self) :
		return self.header





# make for update too


@receiver(post_delete, sender=ImagesOfProducts)
def product_images_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

@receiver(post_delete, sender=Categories)
def categories_images_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)







