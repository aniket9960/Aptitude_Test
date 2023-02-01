from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Enter only Alphabets')
    last_name = forms.CharField(max_length=30, required=False, help_text='Enter only Alphabets')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [ 
            'first_name', 
            'last_name', 
            'email',
            'username', 
            'password1', 
            'password2', 
            ]
def register(response):

    if response.method == "POST":
        form=SignUpForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('Home')
    else:
        form = SignUpForm()
    return render(response,'register/register.html',{"form":form})

def login(response):
    return render(response,'registration/login.html')