from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from Asha.models import BasicDetails,FamilyMembers,Baby,User_Asha_Notifications,User_Pregnancy,User_Palliative
from Staff.models import Asha_Profile,Asha_Contact_User

# Create your views here.


def Home(request):
    user = User.objects.get(username=request.session['username'])
    pro = BasicDetails.objects.get(Auth_Id=user)
    asha = Asha_Profile.objects.get(Auth_Id=pro.Asha_Worker)
    Family = FamilyMembers.objects.filter(Auth_Id=pro.Auth_Id)
    baby = Baby.objects.filter(Auth_Id=pro.Auth_Id)
    pall = User_Palliative.objects.filter(Auth_Id=pro.Auth_Id)
    pre = User_Pregnancy.objects.filter(Auth_Id=pro.Auth_Id)
    return render(request,'User/index.html',{'user':user,'Profile':pro,'asha':asha,'Family':Family,
    'baby':baby,'pall':pall,'pre':pre})
def Contact(request):
    if request.method == "POST":
        Subject = request.POST['Subject']
        Message = request.POST['Query']
        User_Info = request.session['username']

        user = User.objects.get(username=request.session['username'])
        pro = BasicDetails.objects.get(Auth_Id=user)
        asha = Asha_Profile.objects.get(Auth_Id=pro.Asha_Worker)

        contact = Asha_Contact_User(Auth_Id=asha,Status='Send',Subject=Subject,Message=Message,User_Info=User_Info,
        Date=datetime.now())
        contact.save()
        return redirect('Contact')
    else:
        user = User.objects.get(username=request.session['username'])
        msg = Asha_Contact_User.objects.filter(User_Info=request.session['username']).order_by('Date')
        return render(request,'User/Contact.html',{'user':user,'msg':msg})

def User_Notifications(request):
    own = BasicDetails.objects.get(Auth_Id=request.session['username'])
    nots = User_Asha_Notifications.objects.filter(Owner=own.Asha_Worker)
    return render(request,'User/Notifications.html',{'nots':nots})

def Pregnancy(request):
    if request.method == "POST":
        Name = request.POST['name']
        LMP = request.POST['lmp']
        Weeks = request.POST['week']
        Blood = request.POST['blood']
        Weight = request.POST['weight']
        Health = request.POST['health']
        Hospital = request.POST['hospital']
        Doctor = request.POST['doctor']
        Mobile = request.POST['mobile']
        Register_Date = datetime.now()

        own = BasicDetails.objects.get(Auth_Id=request.session['username'])
        data = User_Pregnancy(Auth_Id=own,Name=Name,LMP=LMP,Weeks=Weeks,Blood=Blood,Weight=Weight,Health=Health,
        Hospital=Hospital,Doctor=Doctor,Mobile=Mobile,Register_Date=Register_Date)
        data.save()

        return redirect('UserHome')
    else:
        own = BasicDetails.objects.get(Auth_Id=request.session['username'])
        data = FamilyMembers.objects.filter(Auth_Id=own,Marital='Married',Gender='Female')
        return render(request,'User/Pregnancy.html',{'data':data})


def Palliative(request):
    if request.method == "POST":
        Name = request.POST['name']
        DOB = request.POST['dob']
        Mobile = request.POST['mobile']
        Issue = request.POST['issue']
        Comments = request.POST['comments']
        Register_Date = datetime.now()

        owner = BasicDetails.objects.get(Auth_Id=request.session['username'])

        if Name == owner.Auth_Id:
            data = User_Palliative(Auth_Id=owner,Name=owner.Name,DOB=DOB,Mobile=Mobile,Issue=Issue,
            Comments=Comments,Register_Date=Register_Date)
            data.save()
        else:
            member = FamilyMembers.objects.get(id=Name)
            data = User_Palliative(Auth_Id=owner,Name=member.Name,DOB=DOB,Mobile=Mobile,Issue=Issue,
            Comments=Comments,Register_Date=Register_Date)
            data.save()

        return redirect('UserHome')
    else:
        own = BasicDetails.objects.get(Auth_Id=request.session['username'])
        data = FamilyMembers.objects.filter(Auth_Id=own,Marital='Married')
        return render(request,'User/Palliative.html',{'data':data,'own':own})
