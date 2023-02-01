# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from . import forms,models
from django.views.generic import CreateView
from django.urls import reverse_lazy


def index(request):
    return render(request,'home.html')

def login(request):
    return render(request,'registration/login.html')


def all_categories(request):
    cat_Data = models.QuizCategory.objects.all()
    return render(request,'all-categories.html',{'data':cat_Data})


def category_questions(request,cat_id):
    category = models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestions.objects.filter(category=category).order_by('id').first()
    return render(request,'category-questions.html',{'question':question,'category':category})


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

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'



"""
class RegisterView(CreateView):
    form_class = forms.RegisterUser
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def register(request):
    form = forms.RegisterUser
    msg = None
    if request.method == 'POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg='User Registered'
    return render(request,'registration/register.html',{'form':form,'msg':msg}) """

def easy(request):
    return render(request,'easy.html')

def medium(request):
    return HttpResponse("medium")

def hard(request):
    return HttpResponse("hard")