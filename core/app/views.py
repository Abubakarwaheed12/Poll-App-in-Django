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
            qs=Question.objects.all().annotate(is_user_already_voted=Count("choices__voted_by", filter=Q(choices__voted_by=request.user.id)))
            if request.method=='POST':
                for question in Question.objects.all():
                    ch_id=request.POST.get(f"question-{question.id}")
                    if ch_id:
                          Vote.objects.update_or_create(
                            question=question,
                            user=request.user,
                            defaults={
                                "choice_id": ch_id
                            }
                        )                 
                messages.success(request, 'Your Vote Added Successfully')
            # ch=Choice.objects.all()
            return render(request, 'quiz.html' ,{'questions':qs }) 
        else:
            return redirect('addquesion')
    else:
        return HttpResponseRedirect('accounts/login')
    

# SEARCH FORM 

# function for highlighted 

def highlighted(name, q,c):
    qt=q
    if name.find(qt.title())!=-1:
        qt=q.title()
        c+=name.count(qt.title())
    elif name.find(qt.lower())!=-1:
        qt=q.lower()
        c+=name.count(qt.lower())
    elif name.find(qt.upper())!=-1:
        qt=q.upper()
        c+=name.count(qt.upper())
    return [qt, f'<span style="background-color:red;">{q}</span>' , c]
        

def search(request):
    user=userRoles.objects.get(user=request.user)
    users=User.objects.all()
    q=request.GET.get('q')
    # print(q)
    c=0
    if q:
        users=users.filter(Q(id__contains=q) | Q(username__contains=q) | Q(email__contains=q))
        for user in users:
            [qi,qi_span,c]=highlighted(str(user.id), q, c)
            [qu,qu_span,c]=highlighted(user.username, q, c)
            [qe,qe_span,c]=highlighted(user.email, q, c)
            # print(c)
            
            user.id=str(user.id).replace(qi, qi_span)
            user.username=user.username.replace(qu, qu_span)
            user.email=user.email.replace(qe, qe_span)
    if q==None:
        q=''
    context={
        'users':users,
        'role':user,
        'value':c,
         }
    return render(request, 'search.html' , context=context)

# D