from django import forms
from .models import Question,Score

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
        widgets = {
            'oneScore': forms.RadioSelect(attrs={'display':'inline'}),
            'twoScore': forms.RadioSelect(),
            'threeScore': forms.RadioSelect(),
            'fourScore': forms.RadioSelect(),
            'fiveScore': forms.RadioSelect(),
        }
