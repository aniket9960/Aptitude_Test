from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QuizCategory(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.title
    
class QuizQuestions(models.Model):
    category = models.ForeignKey(QuizCategory,on_delete=models.CASCADE)
    question = models.TextField()
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name_plural='Questions'
        
    def __str__(self):
        return self.question
    
class UserSubmittedAnswer(models.Model):
    question=models.ForeignKey(QuizQuestions,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural='User Submitted Answers'