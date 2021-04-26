from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from Asha.models import BasicDetails
from Staff.models import Asha_Profile

# Create your views here.


def UserHome(request):
    user = User.objects.get(username=request.session['username'])
    pro = BasicDetails.objects.get(Auth_Id=user)
    asha = Asha_Profile.objects.get(Auth_Id=pro.Asha_Worker)

    return render(request,'User/index.html',{'user':user,'Profile':pro,'asha':asha})