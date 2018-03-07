from django.shortcuts import render
from .models import Question,Score
from . import views
from django import forms

def home(request):
    sampleUser = "1"
    sample = Question.objects.current_for_user(sampleUser)
    mod = 0
    if request.user.is_authenticated:
        user = request.user
        questions = Question.objects.current_for_user(user)
        if questions['1']== None or questions['2']== None or questions['3']== None or questions['4']== None or questions['5'] == None:
            mod = 1
    else:
        user = request.user
        questions = Question.objects.current_for_user(sampleUser)
    return render(request,'MC/content.html',{'sample':sorted(sample.items()),'questions':sorted(questions.items()),'mod':mod})

def about(request):
    return render(request,'MC/about.html')

def faq(request):
    return render(request,'MC/FAQ.html')

def resources(request):
    return render(request,'MC/resources.html')

def test(request):
    sampleUser = "1"
    sample = Question.objects.current_for_user(sampleUser)
    mod = 0
    if request.user.is_authenticated:
        user = request.user
        questions = Question.objects.current_for_user(user)
        if questions['1']== None or questions['2']== None or questions['3']== None or questions['4']== None or questions['5'] == None:
            mod = 1
    else:
        user = request.user
        questions = Question.objects.current_for_user(sampleUser)
    return render(request,'MC/test.html',{'sample':sorted(sample.items()),'questions':sorted(questions.items()),'mod':mod})


#allows user to SIGN UP
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

from django.shortcuts import redirect
from .forms import QuestionForm,StatementForm,ScoreForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def statement_input(request,statement,edit):
    user = request.user
    sampleUser = "1"
    questions = Question.objects.current_for_user(user)
    sample= Question.objects.current_for_user(sampleUser)
    if request.method == "POST":
        form = StatementForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.statementNumber=statement
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = StatementForm()

    return render(request,'MC/statement_input.html',{'form': form,'questions': sorted(questions.items()),'statement':statement,'sample':sorted(sample.items()),'edit':edit})

def statement_help(request,state,edits):
    sampleUser = "1"
    sample = Question.objects.current_for_user(sampleUser)
    return render(request,'MC/statementhelp.html',{'sample':sorted(sample.items()),'state':state,'edits':edits})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'MC/question_detail.html',{'question': question})

from django.contrib.auth.models import User

def mycheckup(request):
    user = request.user
    questions = Question.objects.current_for_user(user)
    mod = 0
    if questions['1']== None or questions['2']== None or questions['3']== None or questions['4']== None or questions['5'] == None:
        mod = 1
    return render(request, 'MC/mycheckup.html',{'questions': sorted(questions.items()),'mod':mod})

def url_redirect(request):
    return HttpResponsePermanentRedirect("/MC")

def score(request):
    user = request.user
    questions = Question.objects.current_for_user(user)
    yesno = ((1,"Yes"),(0,"No"),)
    bigfive = ((0,"Really Bad"),
               (1,"Poorly"),
               (2,"Ok"),
               (3,"Pretty Good"),
               (4,"Really Good"),)

    if request.method == "POST":
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            questions = Question.objects.current_for_user(user)
            score.onepk = questions["1"].id
            score.twopk = questions["2"].id
            score.threepk= questions["3"].id
            score.fourpk = questions["4"].id
            score.fivepk = questions["5"].id
            score.author = request.user
            score.save()
            return redirect('scoresheet',pk=score.pk)
    else:
        form = ScoreForm(questions)

    return render(request,'MC/score.html',{'form': form,'questions':questions,'yesno':yesno,'bigfive':bigfive})

def scoresheet (request,pk):
    user = request.user
    scores = Score.user_objects.get_userset(user).count()
    data = Score.data_objects.list(user)
    questions = Question.objects.current_for_user(user)
    bigscorenow = 0
    scorenow = 0
    score2 = 0
    score3 = 0
    date1 ="Not yet completed"
    date2= "Not yet completed"
    date3= "Not yet completed"
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0
    z5 = 0

    import datetime

    if len(data)>2:
        thirdScore = data[2]
        score3 = thirdScore["oneScore"]+thirdScore["twoScore"]+thirdScore["threeScore"]+thirdScore["fourScore"]+thirdScore["fiveScore"]
        score3date = thirdScore["date_created"]
        date3=score3date.strftime('%A %d/%m/%Y')
    if len(data)>1:
        secondScore = data[1]
        score2 = secondScore["oneScore"]+secondScore["twoScore"]+secondScore["threeScore"]+secondScore["fourScore"]+secondScore["fiveScore"]
        score2date = secondScore["date_created"]
        date2=score2date.strftime('%A %d/%m/%Y')
    if len(data)>0:
        lastScore = data.first()
        scorenow = lastScore["oneScore"]+lastScore["twoScore"]+lastScore["threeScore"]+lastScore["fourScore"]+lastScore["fiveScore"]
        bigscorenow = lastScore["bigScore"]
        score1date= lastScore["date_created"]
        date1=score1date.strftime('%A %d/%m/%Y')
        pk1=lastScore["onepk"]
        pk2=lastScore["twopk"]
        pk3=lastScore["threepk"]
        pk4=lastScore["fourpk"]
        pk5=lastScore["fivepk"]
        x1 = Score.objects.filter(author=user,onepk=pk1).count()
        y1=Score.objects.filter(author=user,onepk=pk1,oneScore=1).count()
        z1=round(y1/x1*100,1)
        x2 = Score.objects.filter(author=user,twopk=pk2).count()
        y2=Score.objects.filter(author=user,twopk=pk2,twoScore=1).count()
        z2=round(y2/x2*100,1)
        x3 = Score.objects.filter(author=user,threepk=pk3).count()
        y3=Score.objects.filter(author=user,threepk=pk3,threeScore=1).count()
        z3=round(y3/x3*100,1)
        x4 = Score.objects.filter(author=user,fourpk=pk4).count()
        y4=Score.objects.filter(author=user,fourpk=pk4,fourScore=1).count()
        z4=round(y4/x4*100,1)
        x5 = Score.objects.filter(author=user,fivepk=pk5).count()
        y5=Score.objects.filter(author=user,fivepk=pk5,fiveScore=1).count()
        z5=round(y5/x5*100,1)


    return render(request, 'MC/Scoresheet.html',{'scores':scores,'data':data,'scorenow':scorenow,'date1':date1, 'bigscorenow':bigscorenow, 'score2':score2,'score3':score3,'questions': questions, 'z1':z1, 'z2':z2,'z3':z3,'z4':z4,'z5':z5, 'date2':date2,'date3':date3,'pk':pk})


def otherscore (request,number):
    user = request.user
    data = Score.data_objects.list(user)
    thisscore = data[int(number)]
    otherdate= thisscore["date_created"]
    firstpk = thisscore["onepk"]

    question1 = Question.objects.filter(author=user,pk=thisscore["onepk"]).last()
    question2 = Question.objects.filter(author=user,pk=thisscore["twopk"]).last()
    question3 = Question.objects.filter(author=user,pk=thisscore["threepk"]).last()
    question4 = Question.objects.filter(author=user,pk=thisscore["fourpk"]).last()
    question5 = Question.objects.filter(author=user,pk=thisscore["fivepk"]).last()

    one = thisscore["oneScore"]
    two = thisscore["twoScore"]
    three = thisscore["threeScore"]
    four = thisscore["fourScore"]
    five = thisscore["fiveScore"]

    scorelist=(one,two,three,four,five)
    score = thisscore["oneScore"]+thisscore["twoScore"]+thisscore["threeScore"]+thisscore["fourScore"]+thisscore["fiveScore"]
    bigone= thisscore["bigScore"]

    if bigone==4:
        wellness="Really Good"
    elif bigone==3:
        wellness="Good"
    elif bigone==2:
        wellness="OK"
    elif bigone==1:
        wellness="Bad"
    else:
        wellness="Really Bad"

    question_list = {"1":question1,
                    "2":question2,
                    "3":question3,
                    "4":question4,
                    "5":question5}

    return render(request, 'MC/otherscore.html', {'otherdate':otherdate, 'thisscore':thisscore, 'question_list':question_list, 'score':score,'scorelist':scorelist,'wellness':wellness})


def scorelist (request):
    user = request.user
    scores = Score.user_objects.get_userset(user).count()
    data = Score.data_objects.list(user)
    thislist=[]
    x=0;

    for one in data:
        date=one["date_created"].strftime('%A %d/%m/%Y')
        thislist.append(date)
        x=x+1

    return render (request, 'MC/scorelist.html', {'scores':scores,'data':data,'thislist':thislist})

from django.db.models import Avg
def statement_wellness (request,statement,pk):
    user = request.user
    question = Question.objects.filter(author=user,pk=pk).last()

    if int(statement) == 1:
        score_no=Score.objects.filter(onepk=pk,oneScore=0).aggregate(Avg('bigScore'))
        score_yes=Score.objects.filter(onepk=pk,oneScore=1).aggregate(Avg('bigScore'))
    elif int(statement) == 2:
        score_no=Score.objects.filter(twopk=pk,twoScore=0).aggregate(Avg('bigScore'))
        score_yes=Score.objects.filter(twopk=pk,twoScore=1).aggregate(Avg('bigScore'))
    elif int(statement) == 3:
        score_no=Score.objects.filter(threepk=pk,threeScore=0).aggregate(Avg('bigScore'))
        score_yes=Score.objects.filter(threepk=pk,threeScore=1).aggregate(Avg('bigScore'))
    elif int(statement) == 4:
        score_no=Score.objects.filter(fourpk=pk,fourScore=0).aggregate(Avg('bigScore'))
        score_yes=Score.objects.filter(fourpk=pk,fourScore=1).aggregate(Avg('bigScore'))
    else:
        score_no=Score.objects.filter(fivepk=pk,fiveScore=0).aggregate(Avg('bigScore'))
        score_yes=Score.objects.filter(fivepk=pk,fiveScore=1).aggregate(Avg('bigScore'))

    if score_no["bigScore__avg"] != None:
        total_no=round(((score_no["bigScore__avg"])+1),1)
    else:
        total_no="NO INPUTS!"
    if score_yes["bigScore__avg"] != None:
        total_yes=round(((score_yes["bigScore__avg"])+1),1)
    else:
        total_yes="NO INPUTS!"

    return render(request,'MC/statement_wellness.html',{'question':question,'statement':statement,'total_no':total_no,'total_yes':total_yes,'score_no':score_no})
