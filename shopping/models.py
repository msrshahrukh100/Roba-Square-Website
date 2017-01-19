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
	category = models.CharField(max_length = 200, help_text="Category of Product, eg. Apparels,Clothing")
	image = models.ImageField(upload_to=upload_location_cat, width_field="width_field", height_field="height_field", help_text="Image of the category. It is displayed on the front page. It depicts the category of product")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	category_description = models.TextField(max_length=400, help_text="Description of the category in 400 characters.It is displayed on the front page")
	slug = AutoSlugField(populate_from='category',unique=True)
	link_text = models.CharField(max_length=100, help_text="This text is used for linking the url of the category, eg. Buy Now, Shop Now. ")

	def __unicode__(self) :
		return self.category


	def get_absolute_url(self):
		return reverse("shopping:view_category_or_item", kwargs={"slug": self.slug,"qtype":"categories"})

	class Meta :
		verbose_name = "Categories of Products(Add here)"
		verbose_name_plural = "Categories of Products(Add here)"







#class for storing the product description 
class ProductDescription(models.Model) :
	gender_opt = (('Male','Male'),('Female','Female'),('Unisex','Unisex'),('0','N/A'))

	category = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True,blank=True, related_name="products_desc",help_text="Choose the category of product.")
	name = models.CharField(max_length = 250, help_text="Name of the product, eg.T-shirt, Cup, Hoody, etc.")
	description = models.TextField(blank=True, null=True,help_text="Product description here. Don't include size and color information. Write about product quality , specification, material etc.")
	price = models.PositiveIntegerField(help_text="The price of the product in positive integers")
	stockcount = models.PositiveIntegerField(default=0, help_text="The number of items which are available in the stock")
	gender = models.CharField(max_length=10, choices=gender_opt,help_text="Gender for whom this product is meant for.")
	new_product = models.BooleanField(default=False, help_text="Wether this product is newly added or not. New products are separately displayed on the front page.")
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

	@property
	def get_add_to_wishlist_url(self) :
		return reverse("cart:addtowishlist", kwargs={"id":self.id})


	@property
	def get_delete_cart_url(self) :
		return reverse("cart:deletefromcart", kwargs={"id":self.id})

	@property
	def get_delete_wishlist_url(self) :
		return reverse("cart:deletefromwishlist", kwargs={"id":self.id})

	class Meta :
		verbose_name = "Description of the product(Add here)"
		verbose_name_plural = "Description of the product(Add here)"




#class for storing the list of all products with the variation of size and color
class Products(models.Model) :
	size_opt = (('S','S'),('M','M'),('L','L'),('XL','XL'),('XXL','XXL'),('0','N/A'))

	product = models.ForeignKey(ProductDescription,on_delete=models.CASCADE, null=True, related_name="prod")
	size = models.CharField(max_length=5, choices=size_opt, help_text="Size of the product.")
	color = models.CharField(max_length=30, help_text="Color of the product")
	stockcount = models.PositiveIntegerField(default=0, help_text="The number of items which are available in the stock")

	def __unicode__(self) :
		return str(self.id)

	@property
	def get_image_url(self) :
		return self.productimages.first().image.url

	class Meta :
		verbose_name = "Product"
		verbose_name_plural = "Products"




#upload location for product images
def upload_location_pro(instance,filename) :
	return "product_images/%s/%s" % (instance.product.productimages.name, filename)

#class for storing the product images
class ImagesOfProducts(models.Model) :
	product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='productimages')
	image = models.ImageField(upload_to = upload_location_pro,height_field="height_field", width_field="width_field",help_text="Image showing the different views of the product")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	def __unicode__(self) :
		return str(self.id)

	class Meta :
		verbose_name = "Images of products"
		verbose_name_plural = "Images of products"




def upload_location_sli(instance,filename) :
	return "slider_images/%s"%(filename)

class Slider(models.Model) :
	view_opt = (('center','center'),('left','left'),('right','right'))

	image = models.ImageField(upload_to = upload_location_sli, null=False, blank=False ,height_field="height_field", width_field="width_field",help_text="Images to be displayed on the slider")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	header = models.CharField(max_length=100,help_text="The heading to be displayed on the slider.")
	content = models.CharField(max_length=150,help_text="The text content which is to be displayed on the slider.")
	link_text = models.CharField(max_length=100,help_text="The text which is used to link the url, eg. Buy Now, Shop here .")
	link = models.URLField(max_length=200, help_text="The link of the product or category which is targeted to.")
	alignment = models.CharField(max_length=10 ,choices=view_opt, default="left", help_text="How you wish the text to appear on the slider?")

	def __unicode__(self) :
		return self.header

	class Meta :
		verbose_name = "Images on the slider"
		verbose_name_plural = "Images on the slider"






# make for update too


@receiver(post_delete, sender=ImagesOfProducts)
def product_images_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

@receiver(post_delete, sender=Categories)
def categories_images_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)







