from django.shortcuts import render , HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if  pass1==pass2:
            User.objects.create(username=uname , email=email , password=pass1)
        else:
            return HttpResponse('Your Password Does Not Match')
            

    return render(request, 'login.html')




def signup(request):
    return render(request, 'signup.html')


def logout(request):
    return HttpResponse('husejh')