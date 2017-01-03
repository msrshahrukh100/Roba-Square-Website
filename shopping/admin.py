from django.contrib import admin
import nested_admin
from .models import Categories, ProductDescription, Products, ImagesOfProducts, Slider
# Register your models here.



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
	inlines = [ProductsInline]
	exclude = ("height_field","width_field")


class SliderAdmin(admin.ModelAdmin) :
	exclude = ("height_field","width_field")
	class Meta :
		model = Slider
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(ProductDescription,ProductsDescriptionAdmin)
admin.site.register(Products)
admin.site.register(ImagesOfProducts)
admin.site.register(Slider,SliderAdmin)
