from django.contrib import admin
from .models import Question,Score

admin.site.register(Question)
admin.site.register(Score)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text','author','statementNumber')

#class ScoreAdmin(admin.ModelAdmin):
    #list_display = ('author','oneScore','twoScore','threeScore','fourScore','fiveScore','bigScore','date_created')
