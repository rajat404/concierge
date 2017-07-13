from concierge.base.api.viewsets import NoDeleteModelViewSet

from .models import Answer
from .serializers import AnswerSerializer


class AnswerViewset(NoDeleteModelViewSet):
    queryset = Answer.objects.order_by('id')
    serializer_class = AnswerSerializer
