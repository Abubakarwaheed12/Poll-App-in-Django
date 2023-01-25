from django.shortcuts import render , HttpResponseRedirect , HttpResponse
from app.models import Choice ,Question
from django.contrib import messages
from django.contrib.auth import authenticate

# add question view
def add_question(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            title=request.POST.get('ques')
            ques=Question(title=title)
            ques.save()
            messages.success(request, 'Your Question Was Added SuccessFully')
            return render(request, 'index.html')

        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('accounts/login')

# choice view
def add_choice(request):
    if request.user.is_authenticated:
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
        return HttpResponseRedirect('accounts/login')
# Poll Section view
def All_question(request):
    if request.user.is_authenticated:
        qs=Question.objects.all()
        ch=Choice.objects.all()
        if request.method=='POST':
            for question1 in Question.objects.all():
                ch_id=request.POST.get(str(question1.id))
                voters = [user.id for user in Voter.objects.filter(poll__id=ch_id)]
                if request.user.id in voters:
                    return HttpResponse('you have already voted')   
                else:
                    c=Choice.objects.get(id = ch_id)
                    c.total_votes=c.total_votes + 1
                    c.save()
            messages.success(request, 'Your Vote Added Successfully')
                
        return render(request, 'quiz.html' ,{'question':qs , 'choices':ch}) 
    else:
        return HttpResponseRedirect('accounts/login')