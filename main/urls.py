from django.urls import path
from . import  views 

urlpatterns = [
    path('' , views.index),
    path('aissms/' , views.aissms, name='Aissms'),
    path('home/' , views.index , name='Home'),
    path('about/',views.about,name='About'),
    path('Branches/', views.branches,name='Branches'),
    path('Result-Branches/', views.result_branch,name='Result_Branch'),
    path('all-categories/<int:b_id>', views.all_categories, name='all_categories'),
    path('Result-category/<int:b_id>', views.result_cat, name='result_cat'),
    path('category-questions/<int:b_id>/<int:cat_id>', views.category_questions, name='category_questions'),
    path('submit-answer/<int:cat_id>/<int:b_id>/<int:question_id>', views.submit_answer, name='submit_answer'),
    path('result/<int:b_id>/<int:cat_id>', views.result, name='result'),
    
]
