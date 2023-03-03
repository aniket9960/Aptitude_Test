# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'registration/login.html')

def aissms(request):
    return redirect("https://aissmscoe.com/")

@login_required
def all_categories(request,b_id):
    cat_Data = models.QuizCategory.objects.all()
    return render(request,'all-categories.html',{'data':cat_Data, 'branch_id':b_id})

@login_required
def category_questions(request,b_id,cat_id):
    branch = models.Branches.objects.get(id=b_id)
    category = models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestions.objects.filter(category=category,branch=branch).order_by('id').first()
    request.session['que_count'] += 1
    return render(request,'category-questions.html',{'question':question,'category':category,'branch_id':b_id})

@login_required
def submit_answer(request,cat_id,b_id,question_id):
    
    if request.method=='POST':   
        branch = models.Branches.objects.get(id=b_id)
        category = models.QuizCategory.objects.get(id=cat_id)
        question = models.QuizQuestions.objects.filter(category=category,id__gt=question_id).exclude(id=question_id).order_by('id').first()
        request.session['que_count'] += 1
        
        if 'skip' in request.POST:
            if question:
                quest=models.QuizQuestions.objects.get(id=question_id)
                user=request.user
                answer='Not Submitted'
                models.UserSubmittedAnswer.objects.create(branch=branch,category=category,user=user,question=quest,right_answer=answer)
                return render(request,'category-questions.html',{'question':question,'category':category,'branch_id':b_id})
        else:
            quest=models.QuizQuestions.objects.get(id=question_id)
            user=request.user
            answer=request.POST['answer']
            models.UserSubmittedAnswer.objects.create(branch=branch,category=category,user=user,question=quest,right_answer=answer)
        
        if question and request.session['que_count']<=30:
            return render(request,'category-questions.html',{'question':question,'category':category,'branch_id':b_id})
        else:
            #try making program sleep for 1sec to resolve last skip bug
            result=models.UserSubmittedAnswer.objects.filter(user=request.user,branch=branch,category=category)
            skipped=models.UserSubmittedAnswer.objects.filter(user=request.user,branch=branch,category=category,right_answer='Not Submitted').count()
            attempted=models.UserSubmittedAnswer.objects.filter(user=request.user,branch=branch,category=category).exclude(right_answer='Not Submitted').count()
            
            RightAns = 0
            WrongAns = 0
            for row in result:
                if row.right_answer == row.question.correct_option:
                    RightAns+=1
                else:
                    WrongAns+=1
                     
            return render(request,'result.html',{'result':result,'total_skipped':skipped,'attempted':attempted,'RightAns':RightAns, 'branch':branch, 'category':category,'WrongAns':WrongAns}) 
        
    else:
        return HttpResponse("Method Not Allowed!!!")

def result_branch(request):
    B_Data = models.Branches.objects.all()
    return render(request,'result_branch.html',{'data':B_Data})
 
def result_cat(request,b_id):
    cat_Data = models.QuizCategory.objects.all()
    return render(request,'result_cat.html',{'data':cat_Data, 'branch_id':b_id}) 

@login_required
def branches(request):
    request.session['que_count'] = 0
    B_Data = models.Branches.objects.all()
    return render(request,'branches.html',{'data':B_Data})

@login_required
def result(request,b_id,cat_id):
    branch = models.Branches.objects.get(id=b_id)
    category = models.QuizCategory.objects.get(id=cat_id)
    result=models.UserSubmittedAnswer.objects.filter(user=request.user,branch=branch,category=category)
    skipped=models.UserSubmittedAnswer.objects.filter(user=request.user,branch=branch,category=category,right_answer='Not Submitted').count()
    attempted=models.UserSubmittedAnswer.objects.filter(user=request.user,branch=branch,category=category).exclude(right_answer='Not Submitted').count()
            
    RightAns = 0
    WrongAns = 0
    for row in result:
        if row.right_answer == row.question.correct_option:
            RightAns+=1
        else:
            WrongAns+=1
                     
    return render(request,'result.html',{'result':result,'total_skipped':skipped,'attempted':attempted,'RightAns':RightAns, 'branch':branch, 'category':category,'WrongAns':WrongAns}) 

    