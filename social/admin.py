from django.contrib import admin
from .models import Connections, RecentlyViewed

# Register your models here.
admin.site.register(Connections)

class RecentlyViewedAdmin(admin.ModelAdmin) :
	list_filter = ["timestamp"]
	class Meta :
		model = RecentlyViewed


admin.site.register(RecentlyViewed,RecentlyViewedAdmin)
