from django.db import models
from django.utils import timezone
#from django import forms

# Create your models here.

NUMBER = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)

class QuestionManager(models.Manager):
    def current_for_user(self,user):
        question1 = Question.objects.filter(author=user,statementNumber=1).order_by('-id').first()
        question2 = Question.objects.filter(author=user,statementNumber=2).order_by('-id').first()
        question3 = Question.objects.filter(author=user,statementNumber=3).order_by('-id').first()
        question4 = Question.objects.filter(author=user,statementNumber=4).order_by('-id').first()
        question5 = Question.objects.filter(author=user,statementNumber=5).order_by('-id').first()

        question_list = {"1":question1,
                        "2":question2,
                        "3":question3,
                        "4":question4,
                        "5":question5}
        return question_list

class Question(models.Model):
    statementNumber=models.IntegerField(choices=NUMBER, default='1',verbose_name="The number of the statement")
    text = models.CharField(max_length=500,help_text="Enter your text", verbose_name="New Statement")
    #text = models.TextField(help_text="Enter your Statement")
    author = models.ForeignKey('auth.User')
    date_created = models.DateTimeField(blank=False, null=False)
    objects=QuestionManager()


    def save(self, *args, **kwargs):
        self.date_created = timezone.now()
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.text
