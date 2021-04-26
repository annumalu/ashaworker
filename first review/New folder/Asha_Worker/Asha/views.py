from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from .models import BasicDetails
from Admin.models import State,District,Pan_Mun,Ward
from Staff.models import Asha_Reports,Asha_Profile,Org_Asha_Notifications,Org_Asha_Forms,Asha_Insurance,Asha_Contact_User
import xlwt
# Create your views here.

def AshaHome(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    pend = Asha_Contact_User.objects.filter(Status='Send').count()
    return render(request,'Home.html',{'user':user,'pend':pend})

def Download(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Members.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['User ID', 'Name', 'Gender', 'Address', 'State' , 'District' , 'Panchayath/Muncipality','Ward','Mobile','E-Mail']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = BasicDetails.objects.filter(Asha_Worker=request.session['username']).values_list('Auth_Id', 'Name', 'Gender', 'Address', 'State' , 'Distrct' , 'Pan_Mun','Ward','Phone','Email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
def get_state(request):
    val = list(State.objects.values())
    return JsonResponse({'data':val})

def get_district(request, *args,**kwargs):
    selected_val = kwargs.get('state')
    dist = list(District.objects.filter(State=State.objects.get(id=selected_val)).values())
    return JsonResponse({'data':dist})

def get_pan(request, *args,**kwargs):
    selected_val = kwargs.get('dist')
    pan = list(Pan_Mun.objects.filter(District=District.objects.get(id=selected_val)).values())
    return JsonResponse({'data':pan})

def get_ward(request, *args,**kwargs):
    selected_val = kwargs.get('dist')
    pan = list(Ward.objects.filter(Panchayath=Pan_Mun.objects.get(id=selected_val)).values())
    return JsonResponse({'data':pan})


def Profile(request):
    if request.method == 'POST':
        Auth_Id = request.POST['membership']
        Name = request.POST['fullname']
        Gender = request.POST['gender']
        Address = request.POST['address']
        State_Id = request.POST['state']
        Distrct_Id  = request.POST['district']
        Pan_Mun_Id  = request.POST['panchayath']
        Ward_Id  = request.POST['ward']
        Phone = request.POST['mobile']
        Email = request.POST['email']
        Created_Date = datetime.now()

        request.session['Auth'] = Auth_Id

        state = State.objects.get(id=State_Id)
        dist = District.objects.get(id=Distrct_Id)
        pan = Pan_Mun.objects.get(id=Pan_Mun_Id)
        ward = Ward.objects.get(id=Ward_Id)

        user = User.objects.create_user(username=Auth_Id,password=Auth_Id,email=Email)
        user.save()
        asha = request.session['username']
        data = BasicDetails(Auth_Id=Auth_Id,Asha_Worker=asha,User=user,Name=Name,Address=Address,State=state.State_Name,
        Distrct=dist.District_Name,Pan_Mun=pan.Panchayath_Name,Ward=ward.Ward_Name,Phone=Phone
        ,Email=Email,Created_Date=Created_Date,Gender=Gender)

        data.save()

        messages.success(request,'Profile Created With Auth ID - ' + Auth_Id)

        return redirect('AshaHome')

    else:
        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "MB" + Y + M + D  

        try:
            count = BasicDetails.objects.filter(Auth_Id__contains=X).count()  #Get total number of records
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
        return render(request, 'registration.html',{'ID':X})

def Forms_View(request):
    own = Asha_Profile.objects.get(Auth_Id=request.session['username'])
    form = Org_Asha_Forms.objects.filter(Owner=own.Owner)
    return render(request,'Forms.html',{'form':form})

def Logout(request):
    return redirect('/')


