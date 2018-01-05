from django.shortcuts import render
from .models import Question
from . import views

def home(request):
    return render(request,'MC/content.html')

"""
def link(request):
    return render(request, 'blog/link.html')
"""

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
from .forms import QuestionForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# view for Question template
def new_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'MC/question_edit.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'MC/question_detail.html',{'question': question})

from django.contrib.auth.models import User
#user = User.objects.get(user=request.user)

def all_questions(request):
    user = request.user
    questions = Question.objects.filter(author=user)
    return render(request, 'MC/all_questions.html',{'questions': questions})

def delete_question(request):
    user = request.user
    questions = Question.objects.filter(author=user)
    return render (request,'MC/delete_question.html',{'questions': questions})
