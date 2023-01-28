from django.shortcuts import render , HttpResponse ,redirect ,HttpResponseRedirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,login , logout
from .models import userRoles
# Create your views here.

def loginuser(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user1=authenticate(request,username=uname, password=pass1)
        print(uname,pass1)
        if user1 is not None:
            login(request,user1)
            return redirect('addquesion')
        else:
            return HttpResponse('your password does not match')
    return render(request, 'login.html')




def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        userrole=request.POST.get('role')
        if  pass1!=pass2:
                return HttpResponse('dkjs')
        else:
            myusr=User.objects.create_user(uname ,email ,pass1)
            userRoles.objects.create(user=myusr , is_teacher=userrole == 'Teacher')
            return render(request, 'login.html')

    return render(request, 'signup.html')


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('login')