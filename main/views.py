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
    questions = models.QuizQuestions.objects.filter(category=category)
    return render(request,'category-questions.html',{'data':questions,'category':category})


class RegisterView(CreateView):
    form_class = forms.RegisterUser
    success_url = reverse_lazy('login')
    template_name = 'register.html'



def register(request):
    form = forms.RegisterUser
    msg = None
    if request.method == 'POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg='User Registered'
    return render(request,'registration/register.html',{'form':form,'msg':msg})

def easy(request):
    return render(request,'easy.html')

def medium(request):
    return HttpResponse("medium")

def hard(request):
    return HttpResponse("hard")