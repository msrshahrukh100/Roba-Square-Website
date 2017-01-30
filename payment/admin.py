from django.contrib import admin
from .models import OnlineTransactionsDetail,BuyingCart
# Register your models here.

class OnlineTransactionDetailAdmin(admin.ModelAdmin) :
	list_display = ["user","amount","buyer","buyer_name","purpose","status","timestamp"]
	list_filter = ["timestamp","status"]
	class Meta:
		model = OnlineTransactionsDetail


class BuyingCartAdmin(admin.ModelAdmin) :
	list_display = ["user","product","size","quantity","status","timestamp"]
	list_filter = ["timestamp","status","user","product"]
	class Meta:
		model = BuyingCart


admin.site.register(OnlineTransactionsDetail,OnlineTransactionDetailAdmin)


admin.site.register(BuyingCart, BuyingCartAdmin)
