from concierge.base.api.viewsets import CURLViewSet

from .models import Answer
from .serializers import AnswerSerializer


class AnswerViewset(CURLViewSet):
    queryset = Answer.objects.order_by('id')
    serializer_class = AnswerSerializer
