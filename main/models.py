from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Branches(models.Model):
    title = models.CharField(max_length=100, default='Select Something')
    
    class Meta:
        verbose_name_plural='Branch'
    
    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Type'
    
    def __str__(self):
        return self.title

class QuizCategory(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.title
    
class QuizQuestions(models.Model):
    branch = models.ForeignKey(Branches,on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(QuizCategory,on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type,on_delete=models.CASCADE, null=True)
    question = models.TextField()
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    
    correct_option = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name_plural='Questions'
        
    def __str__(self):
        return self.question
    
class UserSubmittedAnswer(models.Model):
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(QuizCategory,on_delete=models.CASCADE, null=True)
    question=models.ForeignKey(QuizQuestions,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural='User Submitted Answers'
        
""" class UserCategoryAttempts(models.Model):
    category=models.ForeignKey(QuizCategory, on_delete=models.CASCADE)    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    attempt_time=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='User Attempts Category' """