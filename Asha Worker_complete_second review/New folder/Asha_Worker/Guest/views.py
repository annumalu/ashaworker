from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Asha.models import BasicDetails
from .models import Donation
from Guest.Utils import render_to_pdf
from django.views.generic import View
from datetime import datetime
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
def Donate(request):
    if request.method == "POST":
        First_Name = request.POST['firstName']
        Last_Name = request.POST['lastName']
        Email = request.POST['email']
        Addr1 = request.POST['add1']
        Addr2  = request.POST['add2']
        Country  = request.POST['country']
        State  = request.POST['state']
        Pin = request.POST['pin']
        Amount = request.POST['amount']
        Card = request.POST['Card']
        Card_Name = request.POST['cardname']

        data = Donation(First_Name=First_Name,Last_Name=Last_Name,Email=Email,Addr1=Addr1,Addr2=Addr2,
        Country=Country,State=State,Pin=Pin,Card=Card,Card_Name=Card_Name,Amount=Amount)
        data.save()
        return redirect('pdf_view')
    else:
        return render(request,'Guest/Donate.html')
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        Data = Donation.objects.latest('id')
        myDate = datetime.now()
        pdf = render_to_pdf('Print/Invoice.html', {'Data':Data,'Date':myDate,})
        return HttpResponse(pdf, content_type='application/pdf')