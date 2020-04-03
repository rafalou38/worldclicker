from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	pays = CountryField().formfield()
	class Meta:
		model = User
		widgets = {'country': CountrySelectWidget()}
		fields = ['username', 'email', 'password1', 'password2','pays']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	# pays = CountryField().formfield()
	class Meta:
		model = User
		# widgets = {'country': CountrySelectWidget()}
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'pays']
