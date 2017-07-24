# Third Party Stuff
from django.views.generic import ListView, DetailView

from .models import Question, Quiz


class QuizList(ListView):
    model = Quiz


class QuizDetail(DetailView):
    model = Quiz


class QuestionList(ListView):
    model = Question


class QuestionDetail(DetailView):
    model = Question
