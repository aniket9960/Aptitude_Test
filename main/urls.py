from django.urls import path
from . import  views

urlpatterns = [
    path('' , views.index , name='Home'),
    path('account/login',views.login,name='login'),
    path('account/register',views.register,name='register'),
    path('all-categories',views.all_categories, name='all_categories'),
    path('category-questions/<int:cat_id>',views.category_questions, name='category_questions'),
    path('easy/',views.easy, name='Easy'), 
    path('medium/',views.medium, name='Medium'), 
    path('hard/',views.hard, name='Hard'), 
]
