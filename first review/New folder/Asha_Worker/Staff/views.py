from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from .models import Asha_Profile,Asha_Reports,Org_Asha_Notifications,Org_Asha_Forms,Asha_Insurance
from Admin.models import Org_Reports,Org_Profile,Pan_Mun,District,Ward

# Create your views here.

def StaffHome(request):
    if request.method == "POST":
        val = request.POST['keyval']

        basic = Asha_Profile.objects.get(Auth_Id=val)
        print(basic)
        user = User.objects.get(username=basic.Auth_Id)
        
        user.delete()

        return redirect('StaffHome')
    else:
        username = request.session['username']
        user = User.objects.get(username=username)
        prof = Asha_Profile.objects.filter(Owner=username)
        return render(request,'Staff/index.html',{'user':user,'prof':prof})

def Insurance(request):
    ins = Asha_Insurance.objects.all()
    arr = []
    for data in ins:
        if data.Auth_Id.Owner == request.session['username']:
            arr.append(data)
    return render(request,'Staff/Insurance.html',{'ins':arr})


def Reports(request):
    if request.method == "POST":
        Subject = request.POST['subject']
        Comment = request.POST['comment']
        Report = request.FILES['report']

        username = Org_Profile.objects.get(Auth_Id=request.session['username'])

        report = Org_Reports(Auth_Id=username,Subject=Subject,Comment=Comment,Report=Report,Date=datetime.now())
        report.save()
        return redirect('StaffReports')
    else:
        report = Asha_Reports.objects.all()
        return render(request,'Staff/Report.html',{'report':report})


def StaffFeedback(request):
    if 'feedback_btn' in request.POST:
        Feedback = request.POST['feedback']
        Report_id = request.POST['rptid']

        getrpt = Asha_Reports.objects.get(id=Report_id)
        getrpt.Status = "Replied"
        getrpt.Feedback = Feedback
        getrpt.save()

        return redirect('StaffFeedback')
    elif 'form_btn' in request.POST:
        Title = request.POST['subject']
        Comments = request.POST['comment']
        Form = request.FILES['forms']

        username = request.session['username']

        data = Org_Asha_Forms(Owner=username,Title=Title,Form=Form,Comments=Comments,Date=datetime.now())
        data.save()
        return redirect('StaffFeedback')
    elif 'not_btn' in request.POST:
        Title = request.POST['Sub']
        Comments = request.POST['Isu']
        Description = request.POST['Desc']

        username = request.session['username']

        data = Org_Asha_Notifications(Owner=username,Title=Title,Comments=Comments,Description=Description,
        Date=datetime.now())
        data.save()

        return redirect('StaffFeedback')
    else:
        report = Asha_Reports.objects.filter(Status='Not')
        return render(request,'Staff/Feedback.html',{'report':report})


def Add_Asha(request):
    if request.method == "POST":
        first = request.POST['First']
        last = request.POST['Last']
        DOB = request.POST['Dob']
        Gender = request.POST['Gender']
        Qual = request.POST['Qualification']
        Mobile = request.POST['Mobile']
        Aadhar = request.POST['Aadhar']
        Blood = request.POST['Blood']
        Addr1 = request.POST['Ad1']
        Addr2 = request.POST['Ad2']
        Addr3 = request.POST['Ad3']
        Pin = request.POST['Pin']
        Aadhar_Id = request.FILES['Ap_Aadhr_Id']
        Addres_Id = request.FILES['nom_Aadhr_Id']
        Bank_Account = request.POST['account']
        Bank_Name = request.POST['Bankname']
        Account_Number = request.POST['accountnumber']
        IFSC = request.POST['ifsc']
        Branch = request.POST['branch']
        username = request.POST['Email']
        Panchayath_id = request.POST['panch']
        Ward_id = request.POST['wardn']
        Owner = request.session['username']

        pan = Pan_Mun.objects.get(id=Panchayath_id)
        wa = Ward.objects.get(id=Ward_id)

        user = User.objects.create_user(username=username,password=first,email=username,first_name=first,last_name=last)
        user.save()
        
        prof = Asha_Profile(Auth_Id=username,User=user,DOB=DOB,Gender=Gender,Qual=Qual,Mobile=Mobile,Aadhar=Aadhar,
        Blood=Blood,Addr1=Addr1,Addr2=Addr2,Addr3=Addr3,Pin=Pin,Aadhar_Id=Aadhar_Id,Addres_Id=Addres_Id,Bank_Account=Bank_Account,
        Bank_Name=Bank_Name,Account_Number=Account_Number,IFSC=IFSC,Branch=Branch,Panchayath=pan.Panchayath_Name,
        Ward=wa.Ward_Name,Owner=Owner)
        prof.save()


        return redirect('StaffHome')
    else:
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = Y + "as"  + M + D  

        count = User.objects.filter(username__contains=X).count()  #Get total number of records

        
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
        
        X = X + "@gov.com"
        print("==================================")
        print (X)
        return render(request,'Staff/Asha_Woker.html',{'username':X})


def Logout(request):
    return redirect('/')


def get_pan_data(request):
    prof = Org_Profile.objects.get(Auth_Id=request.session['username'])
    dist = District.objects.get(District_Name=prof.District)
    val = list(Pan_Mun.objects.filter(District=dist).values())
    return JsonResponse({'data':val})


def get_json_ward(request, *args,**kwargs):
    selected_val = kwargs.get('state')
    dist = list(Ward.objects.filter(Panchayath=Pan_Mun.objects.get(id=selected_val)).values())
    return JsonResponse({'data':dist})