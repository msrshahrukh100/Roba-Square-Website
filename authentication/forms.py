from django import forms
from .models import UserInformation, Addresses
from django.forms.extras.widgets import SelectDateWidget


class UserInfoForm(forms.ModelForm) :
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	date_of_birth = forms.CharField(required=False)
	date_of_birth.widget=forms.TextInput(attrs={'class': 'datepicker','required':False})
	class Meta :
		model = UserInformation
		fields = ['first_name','last_name','date_of_birth','phonenumber','profession','name_of_institute']
	def clean(self):
		cleaned_data = super(UserInfoForm, self).clean()
		pn = cleaned_data.get('phonenumber',"")
		if pn :
			if len(pn) < 10 or len(pn) > 13 :
				raise forms.ValidationError('Please enter a valid number')
			if len(pn) == 10 and not pn.isdigit() :
				raise forms.ValidationError('Please enter a valid number')
			if len(pn) > 10 and not ('+' in pn) :
				raise forms.ValidationError('Please enter a valid number')
			if len(pn) > 10 and '+' in pn : 
				pn.remove('+')
				if not pn.isdigit() :
					raise forms.ValidationError('Please enter a valid number')

		return self.cleaned_data

class AddressForm(forms.ModelForm) :
	class Meta :
		model = Addresses
		fields = ('address','city','pincode','nearest_landmark')