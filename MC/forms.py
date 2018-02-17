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

    class Meta:
        model = Score

        fields = ('oneScore','twoScore','threeScore','fourScore','fiveScore','bigScore')

        #labels = {'oneScore': questions[0],'twoScore': questions[1],'threeScore': questions[2],'fourScore': questions[3],'fiveScore': questions[4],}

        def __init__(self, questions, *args, **kwargs):
            super().__init__(*args, **kwargs)
            #self.fields('some_field').label = "help!"
            for num, question in questions:
                #self.fields.get('fields').label = question
                self.fields('some_field').label = question

        widgets = {
            'oneScore': forms.RadioSelect,
            'twoScore': forms.RadioSelect(),
            'threeScore': forms.RadioSelect(),
            'fourScore': forms.RadioSelect(),
            'fiveScore': forms.RadioSelect(),
        }

        #labels = {
        #    'oneScore':"YES",
        #}


            #self.fields['oneScore'] = forms.IntegerField()
            #self.fields['oneScore'].label = "New Email Label"

            #labels = {
        #        'oneScore':"YES!",
        #    }
