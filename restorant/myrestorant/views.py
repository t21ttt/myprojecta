from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Feacture
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.
def new1(request):
      if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        food=request.POST['food']
        additional=request.POST['additional']
        amount=request.POST['amount']
        address=request.POST['address']
        message=request.POST['message']
       
        ctx = {
           'name' : name,
           'message' : message,
           'food' :food,
           'additional':additional,
          ' amount':amount,
           'address': address
       }
        message = render_to_string('new1.html',ctx)
        send_mail(name,
        ctx,
        settings.EMAIL_HOST_USER,
        [email], 
        fail_silently=False, html_message=ctx)
   
        
                  
      feactures=Feacture.objects.all()
      return render(request,'new1.html',{'feactures':feactures})


def register(request):
   if request.method=='POST':
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      password2=request.POST['password2']
      username=request.POST['username']
      if password==password2:
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email already used')
            return redirect('register') 
        elif User.objects.filter(username=username).exists():
              messages.info(request,'Username Already Existed')
              return redirect('register')
        else:
              user = User.objects.create_user(username=username,email=email,password=password)
              user.save();
              return redirect('login')
      else:
        messages.info(request,'password is not the same')
        return redirect('register')  
   else:     
      return render(request,'register.html')
def login(request):
  if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')  
        else:
          messages.info(request,'Credentials Invalid') 
          return redirect('login') 
  return render(request,'login.html')