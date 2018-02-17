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

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('text','statementNumber')

class StatementForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('text',)

class ScoreForm(forms.ModelForm):


    def __init__(self, questions, *args, **kwargs):
        #label = {'oneScore':"yes",}
        super().__init__(*args, **kwargs)
        self.fields.get('oneScore').label = questions["1"]
        self.fields.get('twoScore').label = questions["2"]
        self.fields.get('threeScore').label = questions["3"]
        self.fields.get('fourScore').label = questions["4"]
        self.fields.get('fiveScore').label = questions["5"]

        #for num, question in questions.items():
        #    self.fields.get('some_field').label = question

    class Meta:
        model = Score
        fields = ('oneScore','twoScore','threeScore','fourScore','fiveScore','bigScore')


        widgets = {
            'oneScore': forms.RadioSelect,
            'twoScore': forms.RadioSelect(),
            'threeScore': forms.RadioSelect(),
            'fourScore': forms.RadioSelect(),
            'fiveScore': forms.RadioSelect(),
        }

    
