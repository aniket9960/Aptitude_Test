from django.db import models

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
    level = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=10)
    
    
    class Meta:
        verbose_name_plural='Questions'
        
    def __str__(self):
        return self.question