from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from .models import Org_Profile, State, District


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
        return render(request, 'Admin/index.html', {'user': user, 'prof': prof})


def Organizer(request):

        return render(request, 'Admin/Organizer.html', {'username': X, 'state': state})


def Location(request):
    if 'state' in request.POST:
        name = request.POST['State']
        if State.objects.filter(State_Name__iexact=name).exists():
            messages.success(request, 'State Already There!')
        else:
            state = State(State_Name=name)
            state.save()
        return redirect('Location')
    elif 'district' in request.POST:
        name = request.POST['District']
        key = request.POST['state_id']

        if District.objects.filter(District_Name__iexact=name).exists():
            messages.success(request, 'District Already There!')

        else:
            state = State.objects.get(id=key)

            dist = District(State=state, District_Name=name)
            dist.save()
        return redirect('Location')
    else:
        state = State.objects.all()
        return render(request, 'Admin/Location.html', {'state': state})


def get_json_state(request):
    val = list(State.objects.values())
    return JsonResponse({'data':val})

def get_json_district(request, *args,**kwargs):
    selected_val = kwargs.get('state')
    dist = list(District.objects.filter(State=State.objects.get(id=selected_val)).values())
    return JsonResponse({'data':dist})



def Reports(request):

    return render(request, 'Admin/Report.html', {'asha': asha, 'org': org})


def Logout(request):
    return redirect('/')
