from django.shortcuts import render , HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate  , login , logout
# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return HttpResponse('login successfully')
        else:
            return HttpResponse('your password does not match')
    return render(request, 'login.html')




def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if  pass1!=pass2:
                return HttpResponse('dkjs')
        else:
            myusr=User.objects.create_user(uname ,email ,pass1)
            myusr.save()            
            return render(request, 'login.html')

    return render(request, 'signup.html')


def logout(request):
    return HttpResponse('husejh')