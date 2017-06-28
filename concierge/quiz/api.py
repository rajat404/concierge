from concierge.base.api.viewsets import CURLViewSet

from . import models, serializers


class QuestionViewset(CURLViewSet):
    queryset = models.Question.objects.order_by('created')
    serializer_class = serializers.QuestionSerializer


class QuizViewset(CURLViewSet):
    queryset = models.Quiz.objects.order_by('created')
    serializer_class = serializers.QuizSerializer
