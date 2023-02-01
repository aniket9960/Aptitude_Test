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
                return render(request,'category-questions.html',{'question':question,'category':category})
        
        
        if question:
            return render(request,'category-questions.html',{'question':question,'category':category})
        else:
            return HttpResponse("No More Questions")
        
    else:
        return HttpResponse("Method Not Allowed!!!")
