from rest_framework.serializers import ModelSerializer

from shopping.models import Categories

class CategoriesSerializer(ModelSerializer) :
	class Meta:
		model = Categories
		fields = [
		'category_description',
		'image',
		'link_text',
		'link',
		]