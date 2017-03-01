from django.contrib import admin
from .models import Post, PostViews, BlogSlider
# Register your models here.

# class PostAdmin(admin.ModelAdmin) :
# 	change_form_template = 'admin/change_form.html'
# 	class Meta :
# 		model = Post

admin.site.register(Post)
admin.site.register(PostViews)
admin.site.register(BlogSlider)
