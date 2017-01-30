from django.contrib import admin
from .models import OnlineTransactionsDetail
# Register your models here.

class OnlineTransactionDetailAdmin(admin.ModelAdmin) :
	list_display = ["user","amount","buyer","buyer_name","purpose","status","timestamp"]
	list_filter = ["timestamp","status"]
	class Meta:
		model = OnlineTransactionsDetail


admin.site.register(OnlineTransactionsDetail,OnlineTransactionDetailAdmin)
