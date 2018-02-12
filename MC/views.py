from django.shortcuts import render
from .models import Question,Score
from . import views

def home(request):
    sampleUser = "1"
    sample = Question.objects.current_for_user(sampleUser)
    if request.user.is_authenticated:
        user = request.user
        questions = Question.objects.current_for_user(user)
    else:
        user = request.user
        questions = Question.objects.current_for_user(sampleUser)
    return render(request,'MC/content.html',{'sample':sorted(sample.items()),'questions':sorted(questions.items())})

#allows user to SIGN UP
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

from django.shortcuts import redirect
from .forms import QuestionForm,StatementForm,ScoreForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# view for Question template
def new_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'MC/question_edit.html', {'form': form})

def statement_input(request,statement):
    user = request.user
    sampleUser = "1"
    questions = Question.objects.current_for_user(user)
    sample = Question.objects.current_for_user(sampleUser)
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

    return render(request,'MC/statement_input.html',{'form': form,'questions': sorted(questions.items()),'statement':statement,'sample':sorted(sample.items())})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'MC/question_detail.html',{'question': question})

from django.contrib.auth.models import User

def all_questions(request):
    user = request.user
    questions = Question.objects.current_for_user(user)
    return render(request, 'MC/all_questions.html',{'questions': sorted(questions.items())})

def delete_question(request):
    user = request.user
    questions = Question.objects.filter(author=user)
    return render (request,'MC/delete_question.html',{'questions': questions})

#redirect views
def url_redirect(request):
    return HttpResponsePermanentRedirect("/MC")

def score(request):
    user = request.user
    questions = Question.objects.current_for_user(user)

    if request.method == "POST":
        questions = Question.objects.current_for_user(user)
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.author = request.user
            score.onepk = questions["1"].id
            score.twopk = questions["2"].id
            score.threepk= questions["3"].id
            score.fourpk = questions["4"].id
            score.fivepk =questions["5"].id
            score.save()
            return redirect('scoresheet',pk=score.pk)
    else:
        form = ScoreForm()

    return render(request,'MC/score.html',{'form': form,'questions': sorted(questions.items())})

def scoresheet (request,pk):
    user = request.user
    #score = Score.objects.filter(author=user)
    #score = Score.objects.get(author=user)
    scores = Score.user_objects.get_userset(user).count()

    return render(request, 'MC/Scoresheet.html',{'scores':scores})
    #{'scores':sorted(scores.items())),,{'score':sorted(score.items())}
