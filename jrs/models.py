from django.db import models
from datetime import date
import json
import datetime
#from static import ORDER_STATUS
# Create models here.
class StudentData(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	name=models.CharField(max_length=100,default="")
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=8)
	#confirm_password=models.CharField(max_length=8)
	contact_no=models.CharField(max_length=12)
	course=models.CharField(max_length=12,default="")
	semester=models.CharField(max_length=2,default="")
	grade=models.CharField(max_length=2,default="")
	#image=models.ImageField(upload_to="jrs/images",default="")
	newProfilePic=models.FileField(upload_to='jrs', null=True, verbose_name="")

	# def __str__(self):
	# 	return self.email
	def getEmail(self):
		return self.email
#Create your models here.

class ColData(models.Model):
	College_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=8)
	#confirm_password=models.CharField(max_length=8)
	city=models.CharField(max_length=100)
	Contact_no=models.CharField(max_length=12)
	def __str__(self):
		return self.College_name


class ComData(models.Model):
	Company_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=8)
	#confirm_password=models.CharField(max_length=8)
	contact_no=models.CharField(max_length=12)
	city=models.CharField(max_length=100)

	# def __str__(self):
	# 	return self.Company_name
	def getEmail(self):
		return self.email
#Create your models here.

class PostJob(models.Model):
	Job_Designation=models.CharField(max_length=100)
	dob=models.DateField("Date")
	Job_Description=models.CharField(max_length=100)
	end_date=models.DateField("Date")
	contact=models.CharField(max_length=12)
	
	eligibility=models.CharField(max_length=100)
	skills=models.CharField(max_length=100)
	stream=models.CharField(max_length=100)
	company_id=models.ForeignKey(ComData, on_delete=models.CASCADE)
	# def __str__(self):
	# 	return json.dumps({'desig':self.Job_Desigation, 'desc':self.Job_Description})
	def getJobDetails(self):
		dataToBePass=[self.Job_Designation,self.Job_Description]
		return dataToBePass




	


class UploadResume(models.Model):
	Userid=models.ForeignKey(StudentData, on_delete=models.CASCADE)
	Resume_file=models.FileField(upload_to='Documents', null=True)

# class JobApplied(models.Model):
# 	Job_Id=models.ForeignKey(PostJob, on_delete=models.CASCADE)
# 	User_id=models.ForeignKey(StudentData, on_delete=models.CASCADE)
# 	Resume_id=models.ForeignKey(UploadResume , on_delete=models.CASCADE)
# 	status = models.CharField(max_length=50, default="pending")
	

class Apply(models.Model):
	Job_Id=models.ForeignKey(PostJob, on_delete=models.CASCADE)
	Userid=models.ForeignKey(StudentData, on_delete=models.CASCADE)
	# Resume_id=models.ForeignKey(UploadResume , on_delete=models.CASCADE)
	status = models.CharField(max_length=50, default="pending")
	
# class ForStatus(models.Model):
# 	PENDING=0
# 	ACCEPTED=1
# 	REJECTED=3
# 	status_choices(
# 		'PENDING','pending'
# 		'ACCEPTED','accepted'
# 		'SELECTED','selected'
		
# 		)
# 	status=models.PositiveSmallIntegerField(choices=ORDER_STATUS)

# class NotifY(models.Model):
# 	notification=models.CharField(max_length=100,default="")
# 	Job_Id=models.ForeignKey(PostJob, on_delete=models.CASCADE)
# 	student_id=models.ForeignKey(StudentData, on_delete=models.CASCADE)
# 	postedon=models.DateTimeField(null=True)
# 	def __str__(self):
# 		return self.notification

class UserNotify(models.Model):
	notification=models.CharField(max_length=100,default="")
	Job_Id=models.ForeignKey(PostJob, on_delete=models.CASCADE)
	student_id=models.ForeignKey(StudentData, on_delete=models.CASCADE)
	# postedon=models.DateTimeField(null=True)
	# status = 0 Means unread notification
	# status= 1 Notifcatiopn read 
	status=models.CharField(max_length=2, default=0)
	

	# ab apko us bell icon pr click krne ke bad sare 
	# notifications ka status 1 krvan h jo us student se belong krti h
	# nd vha pr mtlb studeadmin page pr fetchkrte time ye dekhna h ki if particular 
	# notification ka status 0 h to uper ornage box aye vrna na aye
	# ok
	postedon=models.CharField(max_length=100, default=datetime.datetime.now())

	def __str__(self):
		return self.notification
		# Done 


