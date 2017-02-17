from django.db import models

# Create your models here.

	
class Leave(models.Model):
    #startDate= models.DateField()
	#endDate= models.DateField()
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

	
class Employee(models.Model):
	
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
	
	
	
	
'''' 
class Department(models.Model):
    name = models.CharField(max_length = 100)

class EmployeeHistory(models.Model):
    employee = models.OneToOneField(Employee)
    date_joined = models.DateField()
    marital_status = models.BooleanField()
	
	'''

