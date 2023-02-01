from django.urls import path
from . import  views

urlpatterns = [
    path('' , views.index , name='Home'),
    path('account/login',views.login,name='login'),
    #path('account/register',views.register,name='register'),
    path('all-categories',views.all_categories, name='all_categories'),
    path('category-questions/<int:cat_id>',views.category_questions, name='category_questions'),
    path('submit-answer/<int:cat_id>/<int:question_id>',views.submit_answer, name='submit_answer'),
    path('account/register',views.SignUpView.as_view(),name='register'),
    
]
