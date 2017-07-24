from django.conf.urls import url
from .views import QuizList, QuizDetail, QuestionList, QuestionDetail

urlpatterns = [
    url(r'^quiz/$', QuizList.as_view(), name='quiz-list'),
    url(r'^quiz/(?P<pk>[0-9a-f-]+)/$', QuizDetail.as_view(), name='quiz-detail'),
    url(r'^question/$', QuestionList.as_view()),
    url(r'^question/(?P<pk>[0-9a-f-]+)/$', QuestionDetail.as_view(), name='question-detail'),
]
