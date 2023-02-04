# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required




def index(request):
    return render(request,'home.html')

def login(request):
    return render(request,'registration/login.html')

@login_required
def all_categories(request):
    cat_Data = models.QuizCategory.objects.all()
    return render(request,'all-categories.html',{'data':cat_Data})

@login_required
def category_questions(request,cat_id):
    category = models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestions.objects.filter(category=category).order_by('id').first()
    return render(request,'category-questions.html',{'question':question,'category':category})

@login_required
def submit_answer(request,cat_id,question_id):
    if request.method=='POST':   
        
        category = models.QuizCategory.objects.get(id=cat_id)
        question = models.QuizQuestions.objects.filter(category=category,id__gt=question_id).exclude(id=question_id).order_by('id').first()
        
        if 'skip' in request.POST:
            if question:
                quest=models.QuizQuestions.objects.get(id=question_id)
                user=request.user
                answer='Not Submitted'
                models.UserSubmittedAnswer.objects.create(user=user,question=quest,right_answer=answer)
                return render(request,'category-questions.html',{'question':question,'category':category})
        else:
            quest=models.QuizQuestions.objects.get(id=question_id)
            user=request.user
            answer=request.POST['answer']
            models.UserSubmittedAnswer.objects.create(user=user,question=quest,right_answer=answer)
        
        if question:
            return render(request,'category-questions.html',{'question':question,'category':category})
        else:
            #try making program sleep for 1sec to resolve last skip bug
            result=models.UserSubmittedAnswer.objects.filter(user=request.user)
            skipped=models.UserSubmittedAnswer.objects.filter(user=request.user,right_answer='Not Submitted').count()
            attempted=models.UserSubmittedAnswer.objects.filter(user=request.user).exclude(right_answer='Not Submitted').count()
            
            RightAns = 0
            for row in result:
                if row.right_answer == row.question.correct_option:
                    RightAns+=1
                    
            
            return render(request,'result.html',{'result':result,'total_skipped':skipped,'attempted':attempted,'RightAns':RightAns})
        
    else:
        return HttpResponse("Method Not Allowed!!!")
