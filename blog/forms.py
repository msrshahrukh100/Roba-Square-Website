from django import forms


from .models import Post



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
		"title",
		"content",
		'show_about_the_author',
		"about_the_author"
		]