from django.contrib import admin
from .models import OnlineTransactionsDetail,OnlineBuyingCart
# Register your models here.

class OnlineTransactionDetailAdmin(admin.ModelAdmin) :
	list_display = ["user","amount","buyer","buyer_name","purpose","status","timestamp"]
	list_filter = ["timestamp","status"]
	class Meta:
		model = OnlineTransactionsDetail


class OnlineBuyingCartAdmin(admin.ModelAdmin) :
	list_display = ["user","product","size","quantity","address","phonenumber","status","timestamp"]
	list_filter = ["timestamp","status","user","product"]
	class Meta:
		model = OnlineBuyingCart


admin.site.register(OnlineTransactionsDetail,OnlineTransactionDetailAdmin)


admin.site.register(OnlineBuyingCart, OnlineBuyingCartAdmin)
