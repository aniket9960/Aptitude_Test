from django.urls import path
from . import  views

urlpatterns = [
    path('home/' , views.index , name='Home'),
    path('all-categories',views.all_categories, name='all_categories'),
    path('category-questions/<int:cat_id>',views.category_questions, name='category_questions'),
    path('submit-answer/<int:cat_id>/<int:question_id>',views.submit_answer, name='submit_answer'),
]
