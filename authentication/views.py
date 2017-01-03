from django.shortcuts import render
from shopping.models import Slider, Categories, ProductDescription

# Create your views here.



def home_page(request) :
	context = {"slider":Slider.objects.all(),
	"categories":Categories.objects.all(),
	"newproducts":ProductDescription.objects.filter(new_product=True)
	}
	return render(request,'index.html',context)

