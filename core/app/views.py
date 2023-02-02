from django.shortcuts import render , HttpResponseRedirect , HttpResponse , redirect
from app.models import Choice ,Question, Vote
from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from accounts.models import userRoles

# add question view
def add_question(request):
    if request.user.is_authenticated:
        role=userRoles.objects.get(user=request.user)
        if role.is_teacher:
            if request.method=='POST':
                title=request.POST.get('ques')
                ques=Question(title=title)
                ques.save()
                messages.success(request, 'Your Question Was Added SuccessFully')
                return render(request, 'index.html')

            return render(request, 'index.html')
        else:
            return redirect('quiz')
    else:
        return HttpResponseRedirect('accounts/login')

# choice view
def add_choice(request):
    if request.user.is_authenticated:
        role = userRoles.objects.get(user=request.user)
        if role.is_teacher:
            if request.method=='POST':
                choice_title=request.POST.get('choice')
                choice_id=request.POST.get('select')
                # get the object of selected choice
                choice_s=Question(id=choice_id)
                Choice.objects.create(question=choice_s , title=choice_title)
                messages.success(request, 'your choice added successfully')
                return render(request, 'index.html')
            else:
                options=Question.objects.all()
                return render(request, 'choice.html' , {'options':options})
        else:
            return redirect('quiz')
    else:
        return HttpResponseRedirect('accounts/login')
# Poll Section view
def All_question(request):
    if request.user.is_authenticated:
        role = userRoles.objects.get(user=request.user)
        if not role.is_teacher:
            ch=Choice.objects.all().annotate(is_user_already_voted=Count("voted_by", filter=Q(voted_by=request.user.id)))
            qs=Question.objects.all()
            if request.method=='POST':
                for question in Question.objects.all():
                    ch_id=request.POST.get(f"question-{question.id}")
                    if ch_id:
                        Vote.objects.create(
                            question=question,
                            choice_id=ch_id,
                            user=request.user
                        )                    
                messages.success(request, 'Your Vote Added Successfully')
            # ch=Choice.objects.all()
            return render(request, 'quiz.html' ,{'questions':qs , 'choices':ch}) 
        else:
            return redirect('addquesion')
    else:
        return HttpResponseRedirect('accounts/login')
    

# SEARCH FORM 

# function for highlighted 

# def  highlighted(name,u):
    

def search(request):
    users=User.objects.all()
    q=request.GET.get('q')
    print(q)
    if q:
        users=users.filter(username__contains=q)
        for user in users:
            user.username=user.username.replace(q, '<span style="background-color:red;">' + q + '</span>')
    if q==None:
        q=''
    context={
        'users':users,
    }
    return render(request, 'search.html' , context=context)