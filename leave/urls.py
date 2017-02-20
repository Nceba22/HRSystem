"""hrproject URL Configuration


"""
from django.conf.urls import url
from . import views 
app_name = 'leave'
urlpatterns = [
    url(r'^index',views.index, name = 'index'),
	
	
	#url(r'^$',views.employee, name = 'employee'),
	#url(r'register/',views.UserFormView.as_view(), name = 'register'),
	
]
