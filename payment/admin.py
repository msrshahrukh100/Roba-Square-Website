from django.contrib import admin
import nested_admin
from .models import OnlineTransactionsDetail,BuyingCart, Refund_requests, RefundsHistory
# Register your models here.

class OnlineTransactionDetailAdmin(admin.ModelAdmin) :
	list_display = ["user","amount","buyer","buyer_name","purpose","status","timestamp"]
	list_filter = ["timestamp","status"]
	class Meta:
		model = OnlineTransactionsDetail


class BuyingCartAdmin(admin.ModelAdmin) :
	list_display = ["user","product","size","quantity","method_of_payment","price","address","phonenumber","status","timestamp","invoice_url"]
	list_filter = ["timestamp","status","user","product","method_of_payment"]
	class Meta:
		model = BuyingCart

# class ReturnsInline(nested_admin.NestedTabularInline) :
# 	model = BuyingCart
# 	extra = 1

class ReturnsAdmin(admin.ModelAdmin) :
	list_display = ["refund_item","item_name","amount","method","reason","order_id","refund_amount_to_user"]
	list_editable = ["refund_amount_to_user"]
	def item_name(self,obj) :
		return obj.refund_item.product.name
	def amount(self,obj) :
		return obj.refund_item.price
	def order_id(self,obj) :
		if obj.refund_item.instamojo_request_id :
			return obj.refund_item.instamojo_request_id
		return obj.refund_item.cod_unique_id
	def method(self,obj) :
		return obj.refund_item.method_of_payment


class RefundHistoryAdmin(admin.ModelAdmin) :
	list_display = ['user','status','body','refund_amount','total_amount','created_at']
admin.site.register(RefundsHistory,RefundHistoryAdmin)

admin.site.register(Refund_requests, ReturnsAdmin)

admin.site.register(OnlineTransactionsDetail,OnlineTransactionDetailAdmin)


admin.site.register(BuyingCart, BuyingCartAdmin)
