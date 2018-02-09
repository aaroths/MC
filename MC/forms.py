from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('text','statementNumber')

class StatementForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('text',)
