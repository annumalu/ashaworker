from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from .models import Org_Profile,State,District,Pan_Mun,Ward,Org_Reports
from Staff.models import Asha_Profile,Asha_Reports

# Create your views here.

def AdminHome(request):
    if request.method == "POST":
        val = request.POST['keyval']

        basic = Org_Profile.objects.get(Auth_Id=val)
        user = User.objects.get(username=basic.Auth_Id)
        
        user.delete()

        return redirect('AdminHome')
    else:
        username = request.session['username']
        user = User.objects.get(username=username)
        prof = Org_Profile.objects.all()
        return render(request,'Admin/index.html',{'user':user,'prof':prof})


def Organizer(request):
    if request.method == "POST":
        first = request.POST['first']
        last = request.POST['last']
        username = request.POST['username']
        gender = request.POST['gender']
        Mobile = request.POST['mobile']
        dob = request.POST['dob']
        img = request.FILES['myimg']
        State_id = request.POST['kerala']
        District_id = request.POST['dist']

        state = State.objects.get(id=State_id)
        district = District.objects.get(id=District_id)

        user = User.objects.create_user(username=username,password=first,email=username,first_name=first,last_name=last,is_staff='1')
        user.save()
        prof = Org_Profile(Auth_Id=username,user=user,DOB=dob,State=state.State_Name,District=district.District_Name,Gender=gender,Mobile=Mobile,image=img)
        prof.save()

        return redirect('AdminHome')
    else:
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = Y + "og"  + M + D  

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
        state = State.objects.all()
        return render(request,'Admin/Organizer.html',{'username':X,'state':state})

def Location(request):
    if 'state' in request.POST:
        name = request.POST['State']
        if State.objects.filter(State_Name__iexact=name).exists():
            messages.success(request,'State Already There!')
        else:
            state = State(State_Name=name)
            state.save()
        return redirect('Location')
    elif 'ward' in request.POST:
        name = request.POST['waname']
        key = request.POST['panch']

        pan = Pan_Mun.objects.get(id=key)

        if Ward.objects.filter(Ward_Name__iexact=name,Panchayath=pan).exists() :
            messages.success(request,'Panchayath/Muncipality Already There!')
        else:
            ward = Ward(Panchayath=pan,Ward_Name=name)
            ward.save()
        return redirect('Location')
    elif 'district' in request.POST:
        name = request.POST['District']
        key = request.POST['state_id']

        if District.objects.filter(District_Name__iexact=name).exists():
            messages.success(request,'District Already There!')
        
        else:
            state = State.objects.get(id=key)

            dist = District(State=state,District_Name=name)
            dist.save()
        return redirect('Location')
    elif 'panchayath' in request.POST:
        name = request.POST['pan_name']
        key = request.POST['dist_id']

        if Pan_Mun.objects.filter(Panchayath_Name__iexact=name).exists():
            messages.success(request,'Panchayath/Muncipality Already There!')
        else:
            dist = District.objects.get(id=key)
        
            pan = Pan_Mun(District=dist,Panchayath_Name=name)
            pan.save()
        return redirect('Location')
    else:
        state = State.objects.all()
        return render(request,'Admin/Location.html',{'state':state})

def get_json_state(request):
    val = list(State.objects.values())
    return JsonResponse({'data':val})

def get_json_district(request, *args,**kwargs):
    selected_val = kwargs.get('state')
    dist = list(District.objects.filter(State=State.objects.get(id=selected_val)).values())
    return JsonResponse({'data':dist})

def get_ward_state_json(request):
    val = list(State.objects.values())
    return JsonResponse({'data':val})

def get_ward_json_district(request, *args,**kwargs):
    selected_val = kwargs.get('state')
    dist = list(District.objects.filter(State=State.objects.get(id=selected_val)).values())
    return JsonResponse({'data':dist})

def get_ward_json_pan(request, *args,**kwargs):
    selected_val = kwargs.get('dist')
    pan = list(Pan_Mun.objects.filter(District=District.objects.get(id=selected_val)).values())
    return JsonResponse({'data':pan})


def Reports(request):
    asha = Asha_Reports.objects.all()
    org = Org_Reports.objects.all()
    return render(request,'Admin/Report.html',{'asha':asha,'org':org})

def Logout(request):
    return redirect('/')
