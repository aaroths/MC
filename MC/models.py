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

class ScoreManager (models.Manager):
    def get_userset(self,user):

        UserScores = Score.objects.filter(author=user)
        #UserScores = Score.objects.filter(author=user).count()

        return UserScores


#class ScoreManager(models.Manager):
#    def current_for_user(self,user):
#        date = Score.objects.filter(author=user,).order_by('-id').first()
#        oneScored = Score.oneScore.filter(author=user).order_by('-id').first()
#        twoScored = Score.twoScore.filter(author=user).order_by('-id').first()
#        threeScored = Score.threeScore.filter(author=user).order_by('-id').first()
#        fourScored = Score.fourScore.filter(author=user).order_by('-id').first()
#        fiveScored = Score.fiveScore.filter(author=user).order_by('-id').first()

#        score_list = {"1":oneScored,
#                        "2":twoScored,
#                        "3":threeScored,
#                        "4":fourScored,
#                        "5":fiveScored,
#                        "6":date}
#        return score_list

class Score(models.Model):

    yesno = ((0,"No"),(1,"Yes"),)
    bigfive = ((0,"Really Bad"),
               (1,"Poorly"),
               (2,"Ok"),
               (3,"Pretty Good"),
               (4,"Really Good"),)

    statementNumber=models.IntegerField(default='1',verbose_name="The number of the statement")
    author = models.ForeignKey('auth.User')
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
    bigScore= models.IntegerField(choices=bigfive, default='3',verbose_name="How are you feeling over the past week?")

    objects = models.Manager()
    user_objects = ScoreManager()

    def save(self, *args, **kwargs):
        self.date_created = timezone.now()
        super(Score, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
