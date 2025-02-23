from django.shortcuts import render,redirect
from django.views import View
from .models import Donor
from .forms import UserForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
def index(request):
    return render(request, "index.html")
class login_donor(View):
    def get(self,request):
        form = LoginForm()
        print("get")
        return render(request, "login-donor.html",locals())
    def post(self,request):
        form = LoginForm(request.POST)
        us = request.POST['username']
        pwd = request.POST['password']
        try:
            user = authenticate(username=us,password=pwd)
            if user:
                donor_user = Donor.objects.filter(user_id=user.id)
                if donor_user:
                    login(request,user)
                    #messages.success(request,'Login Successfully')
                    return redirect('/index-donor')
                else:
                    messages.warning(request,'Invalid Donor User')
            else:
                messages.warning(request,'invalid username and password')

        except:
            messages.warning(request,'Login Failed')
        return render(request,'login-donor.html',locals())
