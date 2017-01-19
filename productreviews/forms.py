from django import forms
from .models import Reviews

class Reviewform(forms.ModelForm) :
	review = forms.CharField(widget=forms.Textarea)
	review.widget=forms.Textarea(attrs={'class':'materialize-textarea','required':False})
	product = forms.CharField(widget=forms.HiddenInput)
	rating = forms.IntegerField()
	rating.widget = forms.TextInput(attrs={'type':'range','min':'1','max':'5'})
	class Meta :
		model = Reviews
		fields = ('product','review','rating')


