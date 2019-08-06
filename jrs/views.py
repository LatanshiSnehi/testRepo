from django.shortcuts import render
from .models import StudentData,ColData,ComData,PostJob,UploadResume,Apply,UserNotify
from django.contrib.auth import logout
from django.http import HttpResponse
import random
import json
import datetime
# from notify.signals import notify

def home(request):
	hom=PostJob.objects.all()
	return render(request, "jrs/home.html",{'hom':hom})
# Create your views here.

def CollegeLogin(request):
	return render(request, "jrs/collegelogin.html")

def CollegeReg(request):
	return render(request, "jrs/collegereg.html")

def CompanyLogin(request):
	if request.session.has_key('email'):
		request.session.flush()
	return render(request, "jrs/companylogin.html")


def CompanyReg(request):
	return render(request, "jrs/companyreg.html")
def stulogin(request):
	if request.session.has_key('email'):
		request.session.flush()
	#return HttpResponse('you are logged out')
	return render(request, "jrs/stulogin.html")
def StudentReg(request):
	return render(request, "jrs/sturegister.html")

def studentAdmin(request):
	if request.session.has_key('email'):
		email1=request.session['email']
		objOne=PostJob.objects.all()
		obj2=StudentData.objects.get(email=email1)
		# print(obj2)
		Appli=Apply.objects.filter(Userid=obj2)
		try:
			noti=UserNotify.objects.filter(student_id=obj2,status='0')
			# print(noti)
			totalNotification=UserNotify.objects.filter(student_id=obj2,status='0').count()
			print("ABCDEFGH===>>"+str(totalNotification))
		except Exception as e:
			noti=[]
			totalNotification=0
		
		
		
		# print(totalNotification)
		return render(request, "jrs/studentadmin.html",{'jobs':objOne,'user':obj2,'Appli':Appli,'noti':noti,'total':totalNotification})
	else:
		return render(request, 'jrs/Stulogin.html')

	 
	
	
def resume(request):
	return render(request, "jrs/resumereg.html")
def ComAdmin(request):
	if request.session.has_key('email'):
		email2=request.session['email']
		obj4=PostJob.objects.all()
		obj5=ComData.objects.get(email=email2)
		obj6=ComData.objects.all()
		obj7=Apply.objects.all()
		return render(request, "jrs/companyadmin.html",{'posts':obj4,'company':obj5,
			'com':obj6,'appp':obj7})
	else:
		return render(request, "jrs/companyadmin.html")


def StuRegisterProcess(request):
	print(request.POST)
	first_name=request.POST['first_name']
	last_name=request.POST['last_name']
	email=request.POST['email']
	password=request.POST['password']
	#confirm_password=request.POST['confirm_password']
	contact_no=request.POST['contact_no']
	obj1=StudentData(first_name=first_name,last_name=last_name,email=email,password=password)
	obj1.save()
	return render(request,'jrs/stulogin.html')

def ColRegPro(request):
	College_name=request.POST['College_name']
	email=request.POST['email']
	password=request.POST['password']
	#confirm_password=request.POST['confirm_password']
	Contact_no=request.POST['Contact_no']
	obj2=ColData(College_name=College_name, email=email, password=password,
	 Contact_no=Contact_no)
	obj2.save()
	return render(request, 'jrs/home.html')

def ComRegisterProcess(request):
	print(request.POST)
	Company_name=request.POST['Company_name']
	email=request.POST['email']
	password=request.POST['password']
	#confirm_password=request.POST['confirm_password']
	contact_no=request.POST['contact_no']
	city=request.POST['city']
	obj3=ComData(Company_name=Company_name,email=email,password=password, contact_no=contact_no,city=city)
	obj3.save()
	return render(request,'jrs/home.html')

def homelog(request):
	if 'email' in request.session:
		print(request.session['email'])
		return render(request,'jrs/home.html')
	else:
		return render(request, 'jrs/stulogin.html')
	return HttpResponse('what is this');
		# total= Question.objects.count()
		# rand= random.randrange(1,total-1)
		# print(rand)
		# print(QuestionId)
		# if len(QuestionId)==0:
		# 	QuestionId.append(rand)
		# else:
		# for x in QuestionId:
		# 	print("value of rand: "+str(rand))
		# 	print("value of X: "+str(x))
		# 	if x!=rand:
		# 		QuestionId.append(rand)
		# 		print(QuestionId)
				
		# 	else:
		# 		print ('Question Already Exists : '+str(x))
		# 		continue
	# d=21
	# for x in QuestionId:
	# 	print("value of D: "+str(d))
	# 	print("value of X: "+str(x))
	# 	if x == d:
	# 		print('Yha to aya hi nhi')
	# 		continue
	# 	else:
	# 		print("Inside For Loop  "+str(x))
def loginValidate(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']

		print(email)
		print(password)
		try:
			objUser=StudentData.objects.get(email=email,password=password)
			email=objUser.getEmail()
			request.session['email']=email
			print('Email: '+request.session['email'])
			code=1

		except Exception as e:
			code=0
	return HttpResponse(json.dumps({'code':code}))

# def formView(request):
#    if request.session.has_key('email'):
# 	  email = request.session['email']
# 	  return render(request, 'studentadmin.html',{"email":email})
#    else:
# 	  return render(request, 'home.html', {})

def loginValidateCom(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']

		print(email)
		print(password)
		try:
			objUser=ComData.objects.get(email=email,password=password)
			email=objUser.getEmail()
			request.session['email']=email
			print('Email: '+request.session['email'])
			code=1
		except Exception as e:
			code=0
	return HttpResponse(json.dumps({'code':code}))
	# return render(request, "companyadmin.html",{{request.StudentData.first_name}})


def logOut(request):
	if request.session.has_key('email'):
		request.session.flush()
	return render(request, 'jrs/stulogin.html')

def logOutC(request):
	if request.session.has_key('email'):
		request.session.flush()
	return render(request, 'jrs/companylogin.html')


'''def StuLog(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		try:
			StudentData.objects.get(email=email,password=password)
			return render(request, dashboard)
		except StudentData.DoesNotExist:
			return render(request, 'jrs/stulogin.html')
	
def ComLog(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		try:
			ColData.objects.get(email=email,password=password)
			return render(request, dashboard)
		except ColData.DoesNotExist:
			return render(request, 'jrs/companylogin.html')

def ColLog(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		try:
			ComData.objects.get(email=email,password=password)
			return render(request, dashboard)
		except ComData.DoesNotExist:
			return render(request, 'jrs/collegelogin.html')'''


def goToDashboard(request):
	return render('jrs/dashboard/index.html')


def AddJob(request):
	print(request.POST)

	Job_Designation=request.POST['Job_Designation']
	dob=request.POST['dob']
	Job_Description=request.POST['Job_Description']
	# comm=request.POST.get('company_id')
	company_id=request.POST['company_id']
	# =ComData.objects.get
	comObj=ComData.objects.get(id=company_id)

  
	end_date=request.POST['end_date']
	contact=request.POST['contact']
	
	eligibility=request.POST['eligibility']
	skills=request.POST['skills']
	stream=request.POST['stream']
	jobs=PostJob(Job_Designation=Job_Designation, dob=dob, Job_Description=Job_Description, 
	 end_date=end_date, contact=contact, eligibility=eligibility, skills=skills, stream=stream, company_id=comObj)
	#cities = City.objects.filter(country_id=country_id).order_by('name')

	jobs.save()
	#entry=PostJob.objects.filter(company_id=company_id).order_by('company_id')
	return render(request, "jrs/companyadmin.html",{'entry':jobs})

def ViewProfile(request):
	# print(request.POST)
	name=request.POST['name']
	email1=request.POST['email']
	contact_no=request.POST['contact_no']
	course=request.POST['course']
	semester=request.POST['semester']
	grade=request.POST['grade']
	stu=StudentData.objects.get(email=email1)
	stu.name=name
	stu.save()
	return render(request, 'jrs/studentadmin.html',{'stud':stu})


def ResumeView(request):
	Userid=request.POST['Userid']
	Resume_file=request.POST['Resume_file']
	resumee=Resume( Userid=Userid,Resume_file=Resume_file)
	resumee.save()
	return render(request, 'jrs/studentadmin.html')
def resumeUpload(request):
	if request.method=='POST':
		res=request.FILES.get('Resume_file')

		user_id=request.POST.get('Userid')
		user=StudentData.objects.get(id=user_id)
		print(res)
		cv=UploadResume(Userid=user, Resume_file=res)
		cv.save()
		return render(request, 'jrs/studentadmin.html' , {'cvv':cv})
	else:
		return render(request, 'not uploaded')
	

def abcd(request):
	if request.method=='POST':
		abc=request.FILES.get('newProfilePic')
		ABC2=request.POST.get('student_id')

		print(abc)
		photo=StudentData.objects.get(id=ABC2)
		photo.newProfilePic=abc
		photo.save()
		return HttpResponse(photo)
	else:
		return HttpResponse("hye")
def JobApply(request):
	Job_Id=PostJob.objects.get(id=request.POST['Job_Id'])
	User_id=StudentData.objects.get(id=request.POST['User_id'])
	# Resume_id=ComData.objects.get(id=request.POST['company_id'])

	#status=request.POST['status']
	app=Apply(Job_Id=Job_Id, Userid=User_id)
	app.save()
	return render(request, 'jrs/studentadmin.html',{'appp':app})
def ForApply(request):
	email2=request.POST.get(Userid)
	apply1=Apply.objects.get(Userid=email2)
	stuResume=UploadResume.objects.get()
	return render(request, "jrs/studentprofile.html",{'details1':apply1})
	

# def status(request):
# 	PENDING=0
# 	ACCEPTED=1
# 	REJECTED=3
# 	choices(
# 		'PENDING','pending'
# 		'ACCEPTED','accepted'
# 		'SELECTED','selected'

# 		)


def StudentProfile(request):
		stuId=request.GET['student_id']
		check=StudentData.objects.get(id=stuId)
		print(check)
		# email2=request.session['email']
		# profile=StudentData.objects.get(email=email2)
		resume=UploadResume.objects.get(Userid=check)

		
		return render(request, "jrs/studentprofile.html",{'details':check,"resume":resume})
	# else:
		# return HttpResponse('NOT DONE')
		
def updateNotiSta(request):
	idd=request.POST['Id']
	studObj=StudentData.objects.get(id=idd)
	notification=UserNotify.objects.filter(student_id=studObj).update(status='1')
	# notification.status=1
	# notification.save()
	return HttpResponse(json.dumps({'code':1}))
def DeleteJob(request):
	# yha pr job idd ayego
	uv=request.GET['job_id']

	objj = PostJob.objects.get(id=uv).delete()
	# objj.delete()
	return HttpResponse('Deleted')
def viewNotice(request):
	notificationId=req

def select(request):
	jobId=request.GET['job_id']

	data=Apply.objects.get(id=jobId)
	data.status="Selected"
	temp=data.save()
	postJobId=data.Job_Id.id
	stuDetail=data.Userid.id
	# #examplestudent id hai 4
	stuDetails=StudentData.objects.get(id=stuDetail)
	jobDetails=PostJob.objects.get(id=postJobId)
	message="You are Selected"
	print(jobDetails)
	dt=datetime.datetime.now()
	# jobDetails=Apply.objects.get(id=jobId)
	print(dt)
	# pos=PostJob.objects.get(id=idd)
	# print("========>"+str(idd))
	dbj=UserNotify(notification=message,Job_Id=jobDetails,student_id=stuDetails,postedon=dt)
	#dbj_read=UserNotify(notification=message,Job_Id=jobDetails,student_id=stuDetails,postedon=dt,status=1)
	#dbj.mark_all_as_read(notification)
	dbj.save()
	# return HttpResponse(jobDetails)
	return render(request, 'jrs/studentadmin.html', {'dbs':dbj})
# def NotiRead(request):
#     status=


def reject(request):
	jobId2=request.GET['job_id']
	data1=Apply.objects.get(id=jobId2)
	data1.status="Rejected"
	data1.save()
	return HttpResponse('rejected')
	


# def forNotify(request):
# 	Job_Id=request.GET['job_id']
# 	jobid=PostJob.objects.get(id=Job_Id)
# 	students=request.GET['student_id']
# 	studentid=StudentData.objects.get(id=students)
	
