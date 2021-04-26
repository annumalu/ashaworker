from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Asha.models import BasicDetails

# Create your views here.

def Home(request):
    return render(request,'Guest/index.html')



def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = auth.authenticate(username=username,password=password)
           
        except:
            user = None
        
        if user is not None and user.is_superuser and user.is_staff:
            auth.login(request,user)
            request.session['username'] = username
            print("------------------------Admin------------------")
            return redirect('AdminHome')
        elif user is not None and user.is_staff:
            auth.login(request,user)
            request.session['username'] = username
            print("------------------------Staff------------------")
            return redirect('StaffHome')
        elif user is not None:
            try:
                basic = BasicDetails.objects.get(Auth_Id=username)
            except:
                basic = None
            
            if basic is None:
                auth.login(request,user)
                request.session['username'] = username
                print("------------------------Asha Worker------------------")
                return redirect('AshaHome')
            else:
                auth.login(request,user)
                request.session['username'] = username
                print("------------------------User------------------")
                return redirect('UserHome')
        elif user is None:
            messages.success(request,'Incorrect Username or Password!')
            return render(request,'Guest/Login.html')
    else:
        return render(request,'Guest/Login.html')


def Register(request):
    if request.method == "POST":
        first_name=request.POST['first']
        last_name=request.POST['last']
        username=request.POST['username']
        password=request.POST['password']

        try:
            user= User.objects.get(username=username)
            messages.success(request,'Username or Email Already Taken')
            return render(request,'Guest/register.html')

        except:
            user=User.objects.create_user(username=username,password=password,email=username,first_name=first_name,last_name=last_name)
            user.save()
            print("Registered")
            #messages.success(request,'User Registered Successfully ! You Can Login Now')
            return redirect('Login')
    else:
        return render(request,'Guest/register.html')
    

def Forgot(request):
    return render(request,'Guest/Forgot.html')