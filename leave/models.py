from django.db import models
from django.db.models import permalink
from django.utils import timezone
import datetime
import datetime as dt
# Create your models here.

	
class Leave(models.Model):
	  
	today = dt.date.today
	endDate = datetime.date(2017,12,30)
	
	def DaysOfLeave(self):
		days =0
		months = 1
		while False: 
			days = endDate.weekday() - today.weekeday()
			print (days % "New")
		else:
			print(days % "declined!")
			
		return days
		
	
		
class Employee(models.Model):
	startDay = dt.date.today
	endDate = datetime.date(2090,12,30)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email_address = models.CharField(max_length=30, db_index=True)
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	
	def LeaveDays(self):
		days =0
		months = 1
		if (days>18) and (months>3): 
			remainder = endDate.weekday() - today.weekeday()
			print(days % "No leave available!")
			
		return days
   
	
	def __unicode__(self):
	
		return '%s' % self.title

    #@permalink
	def get_absolute_url(self):
		
		return ('view_employee', None, { 'slug': self.slug })
	
	'''
    def total_days(self):
		oneday = datetime.timedelta(days=1)
        dat = self.start_date
        total_days = 0
        while(dat <= self.return_date):
            if not dat.isoweekday() in (6, 7):
                total_days += 1
            dat += oneday
        return totaldays
	
		#def leaveStatus(self):
		#	status 
		
'''


	
	
	
	
'''' 
class Department(models.Model):
    name = models.CharField(max_length = 100)

class EmployeeHistory(models.Model):
    employee = models.OneToOneField(Employee)
    date_joined = models.DateField()
    marital_status = models.BooleanField()
	
	'''

