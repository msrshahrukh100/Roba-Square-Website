from django import forms


from .models import Post
from pagedown.widgets import PagedownWidget



class PostForm(forms.ModelForm):
	content = forms.CharField(widget = PagedownWidget())
	class Meta:
		model = Post
		fields = [
		"title",
		"content",
		"image",
		]