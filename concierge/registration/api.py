from concierge.base.api.viewsets import CURLViewSet

from . import models, serializers


class RegistrationAnswerViewset(CURLViewSet):
    queryset = models.RegistrationAnswer.objects.order_by('created')
    serializer_class = serializers.RegistrationAnswerSerializer


class RegistrationQuizViewset(CURLViewSet):
    queryset = models.RegistrationQuiz.objects.order_by('created')
    serializer_class = serializers.RegistrationQuizSerializer
