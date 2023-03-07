from django.contrib import admin
from . import models
# Register your models here.
class BranchesAdmin(admin.ModelAdmin):
    list_display=['id','title']
admin.site.register(models.Branches,BranchesAdmin)
admin.site.register(models.QuizCategory)


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=['branch','category','question','correct_option']
    list_filter =('branch','category')
admin.site.register(models.QuizQuestions,QuizQuestionAdmin)

class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display=['id','question','user','right_answer']
admin.site.register(models.UserSubmittedAnswer,UserSubmittedAnswerAdmin)

""" class UserCategoryAttemptsAdmin(admin.ModelAdmin):
    list_display=['category','user','attempt_time']
admin.site.register(models.UserCategoryAttempts,UserCategoryAttemptsAdmin)
 """
