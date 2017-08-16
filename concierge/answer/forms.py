from django import forms

from .models import Answer
from concierge.quiz.models import Question


class AnswerForm(forms.ModelForm):
    question = forms.ModelMultipleChoiceField(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ('question', 'text_answer', 'choice_answer',)
