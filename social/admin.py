from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Connections, RecentlyViewed, Likes, PicOfTheWeek

# Register your models here.
admin.site.register(Connections)

class RecentlyViewedAdmin(admin.ModelAdmin) :
	list_filter = ["timestamp"]
	class Meta :
		model = RecentlyViewed

class PicOfTheWeekAdmin(AdminImageMixin,admin.ModelAdmin) :
	list_display = ['user','description','image','publish_it']
	list_editable = ['publish_it']
	class Meta :
		model = PicOfTheWeek

admin.site.register(RecentlyViewed,RecentlyViewedAdmin)
admin.site.register(Likes)
admin.site.register(PicOfTheWeek, PicOfTheWeekAdmin)