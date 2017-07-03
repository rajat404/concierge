from concierge.base import response as rsp
from concierge.base.api.mixins import MultiSerializerViewSetMixin
from concierge.base.api.viewsets import CURLViewSet

from .models import Question, Quiz
from .serializers import (QuestionSerializer, QuizSerializer,
                          QuizWriteSerializer)
from .services import create_question, create_quiz


class QuestionViewset(CURLViewSet):
    queryset = Question.objects.order_by('created')
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        create_question(serializer)
        return rsp.Created(serializer.data)


class QuizViewset(MultiSerializerViewSetMixin, CURLViewSet):

    queryset = Quiz.objects.order_by('created')
    serializer_class = QuizSerializer
    serializer_action_classes = {
        'create': QuizWriteSerializer,
    }

    def create(self, request, *args, **kwargs):
        """Quizzes are created immediately after Concourse creation,
        thus Quiz's `create` method doesn't create an instance of Quiz,
        but does create instances of `Question`
        """
        serializer = self.get_serializer(data=request.data)
        create_quiz(serializer)
        return rsp.Created(serializer.data)
