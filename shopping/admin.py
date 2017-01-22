from django.contrib import admin
import nested_admin
from .models import Categories, ProductDescription, Products, ImagesOfProducts, Slider, DetailsOfProducts
# Register your models here.

class DetailsOfProductsInline(nested_admin.NestedTabularInline) :
	model = DetailsOfProducts
	extra = 1

class ImageInline(nested_admin.NestedTabularInline) :
	model = ImagesOfProducts
	exclude = ("height_field","width_field")
	extra = 1

class ProductsInline(nested_admin.NestedTabularInline) :
	model = Products
	inlines = [ImageInline]
	extra = 1

class ProductDescriptionInline(nested_admin.NestedTabularInline) :
	model = ProductDescription
	inlines = [ProductsInline]
	extra = 1

class CategoriesAdmin(nested_admin.NestedModelAdmin) :
	inlines = [ProductDescriptionInline]
	exclude = ("height_field","width_field")


class ProductsDescriptionAdmin(nested_admin.NestedModelAdmin) :
	inlines = [ProductsInline, DetailsOfProductsInline]
	exclude = ("height_field","width_field")


class SliderAdmin(admin.ModelAdmin) :
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


admin.site.register(Categories,CategoriesAdmin)
admin.site.register(ProductDescription,ProductsDescriptionAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(ImagesOfProducts,ImagesOfProductsAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(DetailsOfProducts)
