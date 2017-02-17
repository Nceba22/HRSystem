
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic

from django.template import loader
#from .models import 

class UserFormView(View):
	#form_class = UserForm
	template_name = 'leave/registration_form.html'
	
	#display empty form
	
	def get(self, request):
		form = sel.form_class(None)
		return render(request, self.template_name ("form"/form))

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			
			user = form.save(commit=false)
			username = form.cleaned_date["username"]
			password = form.cleaned_data["password"]
			user.set_password(password)
			user.save()

			#returns User objects if signin is success
			user = authenticate(username=username,password=password)
			#check
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect ("leave:index")
					
		#return render(request, self.template_name ["form":form])
			
		
		
def index(request):
    return HttpResponse ("<h1>Welcome to myHR!</h1>")

def employee (request):
    return render


'''
def index(request):
	return render(request, 'leave/home.html')
'''
