from django.shortcuts import render
from app.models import Choice ,Question
from django.contrib import messages

def add_question(request):
    if request.method=='POST':
        title=request.POST.get('ques')
        ques=Question(title=title)
        ques.save()
        messages.success(request, 'Your Question Was Added SuccessFully')
        return render(request, 'index.html')
            
    return render(request, 'index.html')



def add_choice(request):
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

def All_question(request):
    qs=Question.objects.all()
    ch=Choice.objects.all()
    # if request.method=='POST':
    #     ch1=request.POST.get('question_id')
    #     for i in range(ch1):
    #         Choice(total_votes = vot )
    #         Choice.save()
    return render(request, 'quiz.html' ,{'question':qs , 'choices':ch}) 
