from django import forms
from .models import Question,Score

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        help_texts = {'username': 'Required'}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Must contain at least 8 characters'
        self.fields['password2'].help_text = 'Repeat Password'
        self.fields['email'].help_text = 'Required'

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('text','statementNumber')

class StatementForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('text',)

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('bigScore','oneScore','twoScore','threeScore','fourScore','fiveScore',)
