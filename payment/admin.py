from django.contrib import admin
from .models import OnlineTransactionsDetail,BuyingCart
# Register your models here.

class OnlineTransactionDetailAdmin(admin.ModelAdmin) :
	list_display = ["user","amount","buyer","buyer_name","purpose","status","timestamp"]
	list_filter = ["timestamp","status"]
	class Meta:
		model = OnlineTransactionsDetail


class BuyingCartAdmin(admin.ModelAdmin) :
	list_display = ["user","product","size","quantity","method_of_payment","price","address","phonenumber","status","timestamp"]
	list_filter = ["timestamp","status","user","product","method_of_payment"]
	class Meta:
		model = BuyingCart


admin.site.register(OnlineTransactionsDetail,OnlineTransactionDetailAdmin)


admin.site.register(BuyingCart, BuyingCartAdmin)
