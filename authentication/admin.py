from .models import UserInformation
from django.contrib import admin


class UserinfoAdmin(admin.ModelAdmin):
	list_display = ["user", "date_of_birth","phonenumber","profession","name_of_institute"]
	# list_display_links = ["updated"]
	# list_editable = ["title"]
	# list_filter = ["updated", "timestamp"]

	search_fields = ["user", "phonenumber","profession","name_of_institute"]
	class Meta:
		model = UserInformation



admin.site.register(UserInformation, UserinfoAdmin)