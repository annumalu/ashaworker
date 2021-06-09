from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from .models import BasicDetails, FamilyMembers, Baby,User_Palliative,User_Pregnancy,User_Asha_Notifications
from Admin.models import State, District, Pan_Mun, Ward
from Staff.models import Asha_Reports, Asha_Profile, Org_Asha_Notifications, Org_Asha_Forms, Asha_Insurance, Asha_Contact_User
import xlwt

# Create your views here.

def AshaHome(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    pend = Asha_Contact_User.objects.filter(Status='Send').count()
    return render(request, 'Home.html', {'user': user, 'pend': pend})


def Download(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Members.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['User ID', 'Name', 'Gender', 'Address', 'State', 'District', 'Panchayath/Muncipality', 'Ward', 'Mobile',
               'E-Mail']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = BasicDetails.objects.filter(Asha_Worker=request.session['username']).values_list('Auth_Id', 'Name', 'Gender', 'Address', 'State', 'Distrct', 'Pan_Mun', 'Ward', 'Phone', 'Email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response


def get_state(request):
    val = list(State.objects.values())
    return JsonResponse({'data': val})


def get_district(request, *args, **kwargs):
    selected_val = kwargs.get('state')
    dist = list(District.objects.filter(State=State.objects.get(id=selected_val)).values())
    return JsonResponse({'data': dist})


def get_pan(request, *args, **kwargs):
    selected_val = kwargs.get('dist')
    pan = list(Pan_Mun.objects.filter(District=District.objects.get(id=selected_val)).values())
    return JsonResponse({'data': pan})


def get_ward(request, *args, **kwargs):
    selected_val = kwargs.get('dist')
    pan = list(Ward.objects.filter(Panchayath=Pan_Mun.objects.get(id=selected_val)).values())
    return JsonResponse({'data': pan})


def Profile(request):
    if request.method == 'POST':
        Auth_Id = request.POST['membership']
        Name = request.POST['fullname']
        Gender = request.POST['gender']
        Address = request.POST['address']
        State_Id = request.POST['state']
        Distrct_Id = request.POST['district']
        Pan_Mun_Id = request.POST['panchayath']
        Ward_Id = request.POST['ward']
        Phone = request.POST['mobile']
        Email = request.POST['email']
        Created_Date = datetime.now()

        request.session['Auth'] = Auth_Id

        state = State.objects.get(id=State_Id)
        dist = District.objects.get(id=Distrct_Id)
        pan = Pan_Mun.objects.get(id=Pan_Mun_Id)
        ward = Ward.objects.get(id=Ward_Id)

        user = User.objects.create_user(username=Auth_Id, password=Auth_Id, email=Email)
        user.save()
        asha = request.session['username']
        data = BasicDetails(Auth_Id=Auth_Id, Asha_Worker=asha, User=user, Name=Name, Address=Address,
                            State=state.State_Name,
                            Distrct=dist.District_Name, Pan_Mun=pan.Panchayath_Name, Ward=ward.Ward_Name, Phone=Phone
                            , Email=Email, Created_Date=Created_Date, Gender=Gender)

        data.save()

        messages.success(request, 'Profile Created With Auth ID - ' + Auth_Id)

        return redirect('AshaHome')

    else:
        # Auto Id Generation

        myDate = datetime.now()
        D = myDate.strftime("%d")
        M = myDate.strftime("%m")
        Y = myDate.strftime("%Y")
        X = "MB" + Y + M + D

        try:
            count = BasicDetails.objects.filter(Auth_Id__contains=X).count()  # Get total number of records
        except:
            count = 0

        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
        return render(request, 'registration.html', {'ID': X})


def Forms_View(request):
    own = Asha_Profile.objects.get(Auth_Id=request.session['username'])
    form = Org_Asha_Forms.objects.filter(Owner=own.Owner)
    return render(request, 'Forms.html', {'form': form})


def Profile_Home(request):
    if request.method == "GET":
        Id = request.GET['AuthId']
        try:
            num = BasicDetails.objects.filter(Auth_Id=Id).count()
        except:
            num = 0

        if num == 0:
            messages.success(request, 'Sorry Records Not Found With Auth Id -' + Id)
            return render(request, 'Home.html')
        else:
            Auth = Id
            request.session['Auth'] = Id
            Profile = BasicDetails.objects.get(Auth_Id=Auth)
            Family = FamilyMembers.objects.filter(Auth_Id=Auth)
            baby = Baby.objects.filter(Auth_Id=Auth)
            pall = User_Palliative.objects.filter(Auth_Id=Auth)
            pre = User_Pregnancy.objects.filter(Auth_Id=Auth)
            return render(request, 'Profile_Home.html',{'Profile':Profile,'Family':Family,'baby':baby,
            'pall':pall,'pre':pre})
    else:
        Auth = request.session['Auth']
        Profile = BasicDetails.objects.get(Auth_Id=Auth)
        Family = FamilyMembers.objects.filter(Auth_Id=Auth)
        baby = Baby.objects.filter(Auth_Id=Auth)
        pall = User_Palliative.objects.filter(Auth_Id=Auth)
        pre = User_Pregnancy.objects.filter(Auth_Id=Auth)
        return render(request, 'Profile_Home.html',{'Profile':Profile,'Family':Family,'baby':baby,
        'pall':pall,'pre':pre})


def Main_Home(request):
    Auth = request.session['Auth']
    Profile = BasicDetails.objects.get(Auth_Id=Auth)
    Family = FamilyMembers.objects.filter(Auth_Id=Auth)
    baby = Baby.objects.filter(Auth_Id=Auth)
    pall = User_Palliative.objects.filter(Auth_Id=Auth)
    pre = User_Pregnancy.objects.filter(Auth_Id=Auth)
    return render(request, 'Profile_Home.html', {'Profile': Profile, 'Family': Family, 'baby': baby, 'pall': pall, 'pre': pre})


def Family(request):
    if request.method == 'POST':
        Id = request.session['Auth']
        Name = request.POST['othersname']
        Gender = request.POST['gender']
        Relationship = request.POST['relationship']
        Marital = request.POST['Marital']
        Phone = request.POST['othermobile']

        data = FamilyMembers(Auth_Id=BasicDetails.objects.get(Auth_Id=Id), Name=Name, Gender=Gender,
                             Relationship=Relationship,
                             Marital=Marital, Phone=Phone, Status='Active')
        data.save()
        messages.success(request, 'Family Member Added!')
        return redirect('Main_Home')
    else:
        return render(request, 'Family.html')


def updateFamily(request):
    if request.method == "GET":
        id = request.GET['fieldkey']
        request.session['fieldkey'] = id
        response = FamilyMembers.objects.get(id=id)
        return render(request, 'Update_Family.html', {'response': response})
    elif request.method == "POST":
        data = FamilyMembers.objects.get(id=request.session['fieldkey'])
        data.Name = request.POST['othersname']
        data.Gender = request.POST['gender']
        data.Relationship = request.POST['relationship']
        data.Marital = request.POST['Marital']
        data.Phone = request.POST['othermobile']
        data.save()
        messages.success(request, 'Family Details Updated!')
        return redirect('Main_Home')

def updateprofile(request):
    if request.method == "POST":
        data = BasicDetails.objects.get(Auth_Id=request.session['Auth'])
        data.Phone = request.POST['mobile']
        data.Address = request.POST['address']
        data.Email = request.POST['email']
        data.save()
        messages.success(request,'Profile Updated!')
        return redirect('Main_Home')
    else:
        id = request.session['Auth']
        response = BasicDetails.objects.get(Auth_Id=id)
        return render(request, 'Update_Profile.html',{ 'response':response })


def deleteprofile(request):
    if 'profile' in request.POST:
        Id = request.POST['adhr']
        basic = BasicDetails.objects.get(Auth_Id=Id)
        user = User.objects.get(username=basic.Auth_Id)
        user.delete()
        messages.success(request,'Profile Deleted Associated With Aadhar : ' + Id)
        return redirect('AshaHome')
    elif 'family' in request.GET:
        Id = request.GET['key']
        FamilyMembers.objects.filter(id=Id).delete()
        messages.success(request,'Family Data Deleted')
        return redirect('Main_Home')
    else:
        return render(request,'Profile_Home.html')
def Baby_Register(request):
    if request.method == "POST":
        Name = request.POST['babtismname']
        Gender = request.POST['gender']
        DOB = request.POST['date']

        baby = Baby(Auth_Id=BasicDetails.objects.get(Auth_Id=request.session['Auth']),Name=Name,Gender=Gender,DOB=DOB)
        baby.save()
        return redirect('Main_Home')
    else:
        return render(request,'baptism.html')

def Search(request):
        data = BasicDetails.objects.filter(Asha_Worker=request.session['username'])
        return render(request, 'Search.html', {'data': data})


def Advancedsearch(request):
    if request.method == "GET":
        Name = request.GET.get('result')
        try:
            result = BasicDetails.objects.filter(Name__contains=Name).order_by('Auth_Id').count()
        except:
            result = 0

        data = []
        if result != 0:
            result = BasicDetails.objects.filter(Name__contains=Name).order_by('Auth_Id')
            for i in result:
                fetch = BasicDetails.objects.get(Auth_Id=i.Auth_Id)
                data.append(fetch)
        else:
            messages.success(request, 'Search Results Not Found In Database ! Please Try Again...')

        return render(request, 'Search.html', {'data': data})
    else:
        data = BasicDetails.objects.filter(Asha_Worker=request.session['username'])
        return render(request, 'Search.html', {'data': data})

def Report(request):
        if request.method == "POST":
            Subject = request.POST['subject']
            Comment = request.POST['comment']
            Report = request.FILES['myid']

            username = Asha_Profile.objects.get(Auth_Id=request.session['username'])
            report = Asha_Reports(Auth_Id=username, Status='Not', Subject=Subject, Comment=Comment, Report=Report,
                                  Date=datetime.now())
            report.save()
            return redirect('Report')
        else:
            username = Asha_Profile.objects.get(Auth_Id=request.session['username'])
            data = Asha_Reports.objects.filter(Auth_Id=username)
            return render(request, 'Report.html', {'data': data})

def Contact_User(request):
    if 'search' in request.POST:
        val = request.POST['dist_id']

        data = Asha_Contact_User.objects.get(id=val)
        pend = Asha_Contact_User.objects.filter(Status='Send')
        return render(request,'Contact_User.html',{'data':data,'pend':pend})
    elif 'updt' in request.POST:
        Res = request.POST['res']
        val = request.POST['user_id']

        data = Asha_Contact_User.objects.get(id=val)
        data.Reply = Res
        data.Status = 'Replied'
        data.save()
        return redirect('Contact_User')
    else:
        pend = Asha_Contact_User.objects.filter(Status='Send')
        return render(request,'Contact_User.html',{'pend':pend})
def Notifications_View(request):
    if request.method == "POST":
        Title = request.POST['Subject']
        Message = request.POST['Message']

        username = request.session['username']

        noti = User_Asha_Notifications(Owner=username,Title=Title,Message=Message,Date=datetime.now())
        noti.save()
        return redirect('Notifications')
    else:
        own = Asha_Profile.objects.get(Auth_Id=request.session['username'])
        nots = Org_Asha_Notifications.objects.filter(Owner=own.Owner)
        return render(request,'Notifications.html',{'nots':nots})

def User_Profile(request):
    if request.method == "POST":
        prof = Asha_Profile.objects.get(Auth_Id=request.session['username'])
        ins = Asha_Insurance(Auth_Id=prof,Plan='Life Plan',Amount_Paid='750',Date=datetime.now())
        ins.save()
        return redirect('Profile_Page')
    else:
        prof = Asha_Profile.objects.get(Auth_Id=request.session['username'])
        try:
            ins = Asha_Insurance.objects.get(Auth_Id=prof)
        except:
            ins = 0
        return render(request,'Asha_Profile.html',{'Profile':prof,'ins':ins})

def Logout(request):
    return redirect('/')


