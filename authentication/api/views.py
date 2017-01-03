from rest_framework.generics import ListAPIView
from .serializers import CategoriesSerializer
from rest_framework.renderers import JSONRenderer


from shopping.models import Categories

class HomepageAPIView(ListAPIView) :
	queryset = Categories.objects.all()
	serializer_class = CategoriesSerializer
	# renderer_classes = (JSONRenderer, )
	
