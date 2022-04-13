from pyexpat import model
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View

from .forms import ContactForm
#from mainapp.forms import ContactForm
from . import models
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


# Create your views here.


def home(request):
    return render(request,'index.html')

def services(request):
    return render(request,'service.html')

def technology(request):
    return render(request,'technology.html')

def blog(request):
    return render(request,'blog.html')

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')

def aiml(request):
    return render(request,'ai-service.html')

def odoo(request):
    return render(request,'odoo.html')

def python(request):
    return render(request,'python.html')

def robotic(request):
    return render(request,'Robotic.html')

def BusinessConsulting(request):
    return render(request,'consulting.html')

def BusinessIntelligence(request):
    return render(request,'Business-Intelligence.html')

def hire(request):
    return render(request,'hire.html')

def pwa(request):
    return render(request,'pwa-development.html')

def AI(request):
    return render(request,'ai.html')

def RPA(request):
    return render(request,'rpa.html')

def PythonTechnology(request):
    return render(request,'python-1.html')

def Django(request):
    return render(request,'django.html')

def Golang(request):
    return render(request,'golang.html')

def Flutter(request):
    return render(request,'flutter.html')

def ReactJs(request):
    return render(request,'react.html')

def oddocrm(request):
    return render(request,'blog-1.html')


def aimlblog(request):
    return render(request,'blog-3.html')

def Oddofuture(request):
    return render(request,'blog-2.html')



@csrf_exempt
def Contactdata(request):
    if request.method=='POST':
        
       
       
        name=request.POST['name']
        mobile=request.POST['mobile']
        sender=request.POST['email']
       
       
        
        subject=request.POST['subject']
        message=request.POST['message']

        s=models.contact(name=name,mobile=mobile,email=sender,subject=subject,looking_for=message)
        s.save()
        print(s)
        message=f'Name : {request.POST["name"]}:\n Mobile : {request.POST["mobile"]}:\n Email : {request.POST["email"]}\n Message : {request.POST["message"]}'
        send_mail(subject,message,settings.EMAIL_HOST_USER,['amanpandeyudyalak@gmail.com'],fail_silently=False)
        return redirect('/')
    return render(request,'contact.html')
        
      
        
        
       
        
       


        
    
    

def Blog_1(request):
    return render(request,'blog-1.html')


def Blog_2(request):
    return render(request,'blog-2.html')

def Blog_3(request):
    return render(request,'blog-3.html')


def NewsLetter(request):
    if request.method=='GET':
        subemail=request.GET['sub_email']
        
        if subemail is not None:
            subemail=models.SubscriptionEmail(subemail=subemail)
            subemail.save()
            subject='Thanks'
            message="Thanks for subscribing"
            send_mail(subject,message,settings.EMAIL_HOST_USER,[subemail],fail_silently=False)
    else:
        return HttpResponse('this is form GET')
    return redirect('/')

# @csrf_exempt
# def receivedata(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         mobile=request.POST['mobile']
#         em=request.POST['email']
#         subject=request.POST['subject']
#         message=request.POST['message'],
#         s=models.contact(name=name,mobile=mobile,email=em,subject=subject,looking_for=message)
#         s.save()
#     return render(request,'index.html')
    