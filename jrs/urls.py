from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('CollegeLogin', views.CollegeLogin, name="CollegeLogin"),
    path('CollegeReg', views.CollegeReg, name="CollegeReg"),
    path('CompanyLogin', views.CompanyLogin, name="CompanyLogin"),
    path('CompanyReg', views.CompanyReg, name="CompanyReg"),
    path('CollegeLogin', views.CollegeLogin, name="CollegeLogin"),
    path('CollegeLogin', views.CollegeLogin, name="CollegeLogin"),
    path('resume',views.resume,name="resume"),
    path('stuReg',views.StudentReg, name="stuReg"),
    path('stulogin',views.stulogin, name="stuLogin"),
    path('ComAdmin', views.ComAdmin, name="ComAdmin"),
    path('StuRegisterProcess',views.StuRegisterProcess, name="SturegisterProcess"),
    path('ColRegPro',views.ColRegPro, name="ColRegPro"),
    path('ComRegisterProcess',views.ComRegisterProcess, name="ComRegisterProcess"),
    path('studentAdmin', views.studentAdmin, name="studentAdmin"),
    #path('StuLog', views.StuLog, name="StuLog"),
    #path('ColLog', views.ColLog, name="ColLog"),
    path('logOutC', views.logOutC, name="logOutC"),
    path('logOut', views.logOut, name="logOut"),
    path('dasboard', views.goToDashboard, name="dasboard"),
    path('homelog', views.homelog, name="homelog"),
    path('loginValidate', views.loginValidate, name="loginValidate"),
    path('loginValidateCom', views.loginValidateCom, name="loginValidateCom"),
    path('AddJob', views.AddJob, name="AddJob"),
    #path('formView', views.formView, name="formView"),
    path('StudentProfile', views.StudentProfile, name="StudentProfile"),
    path('ViewProfile', views.ViewProfile, name="ViewProfile"),
    path('ResumeView', views.ResumeView, name="ResumeView"),
    path('abcd', views.abcd, name="abcd"),
    path('resumeUpload', views.resumeUpload, name="resumeUpload"),
    path('JobApply', views.JobApply, name="JobApply"),
    path('ForApply', views.ForApply, name="ForApply"),
    path('DeleteJob', views.DeleteJob, name="DeleteJob"),
    path('select', views.select, name="select"),
    path('reject', views.reject, name="reject"),
    path('updateNotiSta', views.updateNotiSta, name="updateNotiSta"),
    

  
  
    

    

 ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)