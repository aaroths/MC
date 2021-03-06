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
    text = models.CharField(max_length=500,help_text="Enter Your Statement", verbose_name="")
    #text = models.TextField(help_text="Enter your Statement")
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    date_created = models.DateTimeField(blank=False, null=False)
    objects=QuestionManager()


    def save(self, *args, **kwargs):
        self.date_created = timezone.now()
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.text

class ScoreManager (models.Manager):
    def get_userset(self,user):

        UserScores = Score.objects.filter(author=user)
        #UserScores = Score.objects.filter(author=user).count()

        return UserScores


class DataManager (models.Manager):
    def list(self,user):
        result_list=Score.objects.filter(author=user).values().order_by("-id")
        return result_list

class Score(models.Model):

    yesno = ((1,"Yes"),(0,"No"),)
    bigfive = ((0,"Really Bad"),
               (1,"Bad"),
               (2,"Ok"),
               (3,"Good"),
               (4,"Really Good"),)

    statementNumber=models.IntegerField(default='1',verbose_name="The number of the statement")
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    date_created = models.DateTimeField(blank=False, null=False)
    onepk=models.IntegerField(default='1')
    twopk=models.IntegerField(default='1')
    threepk=models.IntegerField(default='1')
    fourpk=models.IntegerField(default='1')
    fivepk=models.IntegerField(default='1')
    oneScore = models.IntegerField(choices=yesno,default='none',verbose_name="statement 1")
    twoScore = models.IntegerField(choices=yesno, default='none',verbose_name="statement 2")
    threeScore = models.IntegerField(choices=yesno, default='none',verbose_name="statement 3")
    fourScore= models.IntegerField(choices=yesno, default='none',verbose_name="statement 4")
    fiveScore= models.IntegerField(choices=yesno, default='none',verbose_name="statement 5")
    bigScore= models.IntegerField(choices=bigfive, default='3',verbose_name="How were you feeling?")

    objects = models.Manager()
    user_objects = ScoreManager()
    data_objects = DataManager()

    def save(self, *args, **kwargs):
        self.date_created = timezone.now()
        super(Score, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
