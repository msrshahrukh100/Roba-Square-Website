from django.contrib import admin
from .models import Post, PostViews, BlogSlider
# Register your models here.

# class PostAdmin(admin.ModelAdmin) :
# 	change_form_template = 'admin/change_form.html'
# 	class Meta :
# 		model = Post

class PostViewsAdmin(admin.ModelAdmin) :
	list_display = ['post','user','ip','viewed_on']
	class Meta :
		model = PostViews

admin.site.register(Post)
admin.site.register(PostViews, PostViewsAdmin)
admin.site.register(BlogSlider)
