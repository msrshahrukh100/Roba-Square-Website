from django.contrib import admin
from .models import Reviews, ProductSuggestions
# Register your models here.

class ReviewModelAdmin(admin.ModelAdmin):
	list_display = ["user", "product", "rating"]
	list_filter = ["rating"]

	class Meta:
		model = Reviews

class ProductSuggestionsAdmin(admin.ModelAdmin) :
	list_display = ["user", "content", "email"]

	class Meta:
		model = ProductSuggestions



admin.site.register(Reviews, ReviewModelAdmin)
admin.site.register(ProductSuggestions, ProductSuggestionsAdmin)
