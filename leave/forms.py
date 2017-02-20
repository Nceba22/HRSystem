from django.contrib.auth.models import User
from django import forms

#make new user form class
class UserForm(forms.ModelForm)
	password = forms.CharField(widget=forms.PasswordInput) #ensure password 
	class Meta: #meta class information
		model = User 
		fields = ['surname', 'email', 'password']