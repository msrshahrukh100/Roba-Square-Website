from django.contrib import admin
import nested_admin
from .models import Categories, ProductDescription, Products, ImagesOfProducts, Slider, DetailsOfProducts,ProductRelationsForLogo, BulkOrders
from sorl.thumbnail.admin import AdminImageMixin
# Register your models here.

class DetailsOfProductsInline(AdminImageMixin,nested_admin.NestedTabularInline) :
	model = DetailsOfProducts
	extra = 1

class ImageInline(AdminImageMixin,nested_admin.NestedTabularInline) :
	model = ImagesOfProducts
	exclude = ("height_field","width_field")
	extra = 1

class ProductsInline(AdminImageMixin,nested_admin.NestedTabularInline) :
	model = Products
	inlines = [ImageInline]
	extra = 1

class ProductDescriptionInline(AdminImageMixin,nested_admin.NestedTabularInline) :
	model = ProductDescription
	inlines = [ProductsInline]
	extra = 1

class CategoriesAdmin(AdminImageMixin,nested_admin.NestedModelAdmin) :
	inlines = [ProductDescriptionInline]
	exclude = ("height_field","width_field")


class ProductsDescriptionAdmin(AdminImageMixin,nested_admin.NestedModelAdmin) :
	inlines = [ProductsInline, DetailsOfProductsInline]
	exclude = ("height_field","width_field")


class SliderAdmin(AdminImageMixin ,admin.ModelAdmin) :
	exclude = ("height_field","width_field")
	list_display = ["header", "content","link_text","link","alignment"]
	list_editable = ["header", "content","link_text","link","alignment"]
	list_display_links = []
	class Meta :
		model = Slider

class ImagesOfProductsAdmin(admin.ModelAdmin) :
	exclude = ("height_field","width_field")
	list_display = ["product","image"]
	class Meta:
		model = ImagesOfProducts

class ProductsAdmin(admin.ModelAdmin) :
	list_display = ["product","size","color","stockcount"]
	class Meta:
		model=Products

class BulkOrdersAdmin(AdminImageMixin,admin.ModelAdmin) :
	list_display = ['product','base','user_email','phone','quantity','description','image']
	class Meta :
		model = BulkOrders

	def user_email(self,obj) :
		return obj.user.email

admin.site.register(Categories,CategoriesAdmin)
admin.site.register(ProductDescription,ProductsDescriptionAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(ImagesOfProducts,ImagesOfProductsAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(DetailsOfProducts)
admin.site.register(ProductRelationsForLogo)
admin.site.register(BulkOrders,BulkOrdersAdmin)
